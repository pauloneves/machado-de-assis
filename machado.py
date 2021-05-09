#!/bin/env python

import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
import re
from pathlib import Path

import slugify
from bs4 import BeautifulSoup, Comment, Tag, NavigableString
from ebooklib import epub

import capa

nonAdjustableSpace = "\u2005"


class ErroFormatacao(RuntimeError):
    pass


def get_livro(filename="livros/Papéis avulsos_files/tx_Papeisavulsos.html"):
    with open(filename, encoding="cp1252") as f:
        tudo = f.read()
        # tudo = faz_correcoes_gerais(tudo, filename)
        livro = BeautifulSoup(tudo, "html.parser")
    return livro


def find_titulo_contos(text):
    return isinstance(text, Comment) and text.strip().startswith("*******")


def get_nome_livro(livro) -> str:
    return capitaliza(livro.title.string)


def limpa_h2(livro):
    return
    for h2 in livro.find_all("h2"):
        while True:
            n = h2.next_sibling
            if n.string:
                n.extract()
            else:
                break


def ajusta_titulo_livro(livro):
    p = capitaliza_soup(livro.find("p"))
    p.name = "h1"
    del p.attrs["align"]
    autor = p.find_next("p")
    del autor.attrs["align"]
    notas = autor.find_next("p")
    notas.name = "h2"
    del notas.attrs["align"]

    secao = livro.find("div", {"class": "section"})
    ajusta_secao(secao)

    preambulo = secao.find_next("div", {"class": "section"})
    ajusta_secao(preambulo)
    preambulo.p.name = "h2"


def pg_break(b):
    return b.new_tag(name="mpb:pagebreak")


def ajusta_titulos_contos(livro: BeautifulSoup):
    """Títulos dos contos viram <H2>
    limpa excesso de divs
    """
    comentarios_titulo = livro.find_all(text=find_titulo_contos)

    for titulo in comentarios_titulo:
        secao = titulo.find_next("div", {"class": "section"})
        ajusta_secao(secao)

        header = capitaliza_soup(titulo.find_next("p"))
        header.name = "h2"
        del header.attrs["align"]
        if header:
            sup = list(secao.parents)[-1].new_tag("sup")
            a = header.find(lambda tag: tag.name == "a" and "*" in tag.string)
            if a:
                a.wrap(sup)
                a.string = "*"  # tira espaços
        secao.insert_before(pg_break(livro))


def ajusta_secao(secao: BeautifulSoup, subsection=False):
    if "lang" in secao.attrs:
        del secao.attrs["lang"]
    div_inicial = secao.parent.parent.parent.parent
    if div_inicial:
        div_inicial.replace_with(secao)
        if subsection:
            secao.attrs["class"] = "subsection"


def ajusta_titulos_capitulos(livro: BeautifulSoup):
    def nao_fecha_p_capitulo(p):
        return len(p) > 2 and p[1].p

    for secao in livro.find_all("div", {"class": "section"}):
        p = secao.find_all("p")
        # capítulo começa com 2 parágrafos centralizados
        if (
            len(p) > 1
            and p[0].attrs.get("align") == "center"
            # and p[1].attrs.get("align") == "center"
        ):
            ajusta_secao(secao, subsection=True)

            if nao_fecha_p_capitulo(p):
                raise ErroFormatacao(
                    f"Erro! Não fecha tag <p> no capítulo '{p[0].text}'"
                )

            h3 = livro.new_tag("h3")
            h3.append(p[0].b)
            if p[1].attrs.get("align") == "center" and p[1].b is not None:
                h3.append(livro.new_tag("br"))
                h3.append(p[1].b)

            p[0].insert_before(capitaliza_soup(h3))
            p[0].decompose()
            p[1].decompose()


def parse_nota(nota: BeautifulSoup):
    id_ = re.search(r"icon: \$\('([^']+)", nota.string).group(1)
    texto = re.search(r"content: '([^']+)", nota.string).group(1)
    return id_, texto


def get_notas_dict(livro):
    notas = []
    for nota in livro.find_all("script"):
        if nota.string and "HelpBalloon(" in nota.string:
            notas.append(parse_nota(nota))
    return dict(notas)


def ajusta_referencia(ref: BeautifulSoup):
    attrs = ref.attrs
    assert "href" in attrs and "id" in attrs and "onclick" in attrs, f"{ref} {attrs}"
    attrs["href"] = f"notas.html#{attrs['id']}"
    attrs["id"] = f"orig_{attrs['id']}"
    attrs["epub:type"] = "noteref"
    del attrs["onclick"]


def ajusta_todas_referencias(livro: BeautifulSoup):
    for a in livro.find_all("a", href="#"):
        ajusta_referencia(a)


def link_back_nota(nota, livro) -> str:
    ref_orig = livro.find("a", id=f"orig_{nota}")
    if not ref_orig:
        print(f"Não achei volta {nota}")
        return ""
    capitulo = ref_orig.find_previous(["h2", "h1"])
    cap_filename = get_capitulo_filename(capitulo)
    return f"{cap_filename}#orig_{nota}"


def append_notas(livro: BeautifulSoup, notas: dict):
    section = livro.new_tag("div")
    section.attrs["class"] = ["section"]
    h2 = livro.new_tag("h2")
    h2.append("Notas")
    section.append(h2)
    livro.body.append(pg_break(livro))
    for nota, texto in notas.items():
        # note = livro.new_tag("p")
        aside = livro.new_tag("aside", id=nota, **{"epub:type": "footnote"})
        aside.append("● ")
        aside.append(BeautifulSoup(texto, "html.parser"))

        refback = livro.new_tag("a", href=link_back_nota(nota, livro))

        refback.append(" ☚ ")
        aside.append(refback)
        # section.append(note)
        section.append(aside)
    livro.body.append(section)


def reorganiza_notas(livro):
    assert len(livro.find_all("h2")) > 0, "Primeiro tem que chamar 'ajusta_titulos'"

    notas = get_notas_dict(livro)
    ajusta_todas_referencias(livro)
    append_notas(livro, notas)


def prepara_toc(livro):
    toc = []

    n_h2 = 1
    n_h3 = 1
    for header in livro.find_all(["h2", "h3"]):
        if header.name == "h2":
            the_id = f"{n_h2}"
            n_h2 += 1
            n_h3 = 1
            toc.append((the_id, header.string, []))
        else:
            the_id = f"{n_h2-1}.{n_h3}"
            n_h3 += 1
            toc[-1][-1].append((the_id, header.string))
        header.attrs["id"] = the_id
    return toc


def cria_toc(livro, nome_arq):
    toc = prepara_toc(livro)

    toc_div = livro.new_tag("div", id="toc")
    for ref, titulo, sub_capitulos in toc:
        capitulo = toc_div.new_tag("a", href=f"#{ref}")
        capitulo.append(titulo)
        toc_div.append(capitulo)

        for sub_ref, sub_titulo in sub_capitulos:
            sub_capitulo = toc_div.new_tag("a", href=f"#{sub_ref}")
            sub_capitulo.append(sub_titulo)
            toc_div.append(sub_capitulo)

    livro.body.insert(0, toc_div)

    h2 = livro.new_tag("h2")
    h2.append("Índice")
    livro.body.insert(0, h2)


def limpa_scripts(livro):
    for script in livro.find_all("script"):
        script.decompose()


def processa_livro(filename="livros/Papéis avulsos_files/tx_Papeisavulsos.html"):
    livro = get_livro(filename)
    ajusta_titulos(livro)
    reorganiza_notas(livro)
    limpa_scripts(livro)
    prepara_toc(livro)
    return livro


def ajusta_titulos(livro):
    ajusta_titulo_livro(livro)
    ajusta_titulos_contos(livro)
    ajusta_titulos_capitulos(livro)
    limpa_h2(livro)


def valida_estrutura(livro):
    # __import__("ipdb").set_trace()
    assert not len(
        livro.find_all("div", {"class": "section", "lang": "de"})
    ), "depois de ajustar todos os títulos não pode sobrar seções com lang"


def get_capitulo_filename(header) -> str:
    return slugify.slugify(header.text) + ".html"


def gera_ebook(livro):
    titulo = get_nome_livro(livro)
    book = epub.EpubBook()
    book.set_identifier("22061970ni")
    book.set_title(titulo)
    book.set_language("pt")
    book.add_author("Machado de Assis")

    capa_filename = capa.gera_capa(titulo)
    with open(capa_filename, "rb") as f:
        book.set_cover(capa_filename, f.read())

    # define css style
    with open("style.css", "r", encoding="utf-8") as f:
        style = f.read()

    # add css file
    nav_css = epub.EpubItem(
        uid="style_nav",
        file_name="style/style.css",
        media_type="text/css",
        content=style,
    )
    book.add_item(nav_css)

    capitulos = []
    content = ""
    capitulo = None
    toc = []
    for section in livro.find_all("div", {"class": ["section", "subsection"]}):
        if section.attrs["class"] == ["section"]:
            if content:
                capitulo.set_content(faz_correcoes_gerais(content))
                content = ""

            capitulo = epub.EpubHtml(
                title=limpa_titulo(section.h2),
                file_name=get_capitulo_filename(section.h2),
                media_type="text/html",
            )
            capitulo.add_item(nav_css)
            book.add_item(capitulo)
            capitulos.append(capitulo)
            toc.append(
                [epub.Section(title=capitulo.title, href=capitulo.file_name), []]
            )
            # não pode ter pretiffy que coloca espaços espúrios nos links
            content = str(section)
        else:  # subsection
            content += "\n\n" + str(section)
            h3_id = section.find("h3").attrs["id"]

            # primeira subsection/capítulo do conto fica na seção inicial do conto
            if toc[-1][1] == []:
                first_id = h3_id.split(".")[0] + ".1"
                primeiro_capitulo = extrai_subtitulo(
                    BeautifulSoup(content, "html.parser").h3
                )
                toc[-1][1].append(
                    epub.Link(
                        href=f"{capitulo.file_name}#{first_id}",
                        title=primeiro_capitulo,
                        uid="",
                    )
                )

            toc[-1][1].append(
                epub.Link(
                    href=f"{capitulo.file_name}#{h3_id}",
                    title=extrai_subtitulo(section.h3),
                    uid="",
                )
            )
    capitulo.set_content(faz_correcoes_gerais(content))

    book.toc = toc

    # add navigation files
    epub_nav = epub.EpubNav()
    epub_nav.add_item(nav_css)
    book.add_item(epub.EpubNcx())
    book.add_item(epub_nav)

    # create spine
    book.spine = ["nav"] + capitulos

    # create epub file
    epub.write_epub(f"kindle/{titulo}.epub", book)


def limpa_titulo(titulo_tag: Tag) -> str:
    titulo = capitaliza_soup(titulo_tag).text.strip(" \n*'$")
    if "FASE" in titulo:
        titulo = re.search(r"(.*FASE[- ()0-9]+)", titulo).group(1)
    return titulo


def processa(arq):
    livro = processa_livro(arq)
    with open(f"kindle/livro_alterado_{get_nome_livro(livro)}.html", "w") as file:
        file.write(livro.prettify())
    valida_estrutura(livro)
    gera_ebook(livro)


def extrai_subtitulo(h3):
    return " ".join([c.strip() for c in h3.find_all(text=True)])


def substitui_travessao(text: str) -> str:
    # não casa qdo o travessão no início da linha
    # na prática sempre tem pelo menos um <p> antes do traverssão
    text = re.sub(r"<p>\s*-\s+", r"<p>—" + nonAdjustableSpace, text)
    text = re.sub(r'([^-])-\s*(?=[ .;, ":])', r"\1—", text)
    return text


def conserta_aspas(text: str) -> str:
    # substitui aspas de html:
    text = re.sub('"(?=[^<]*>)', "§¢¬", text)
    # conserta aspas genéricas
    text = re.sub(r'"([^"]*?)"', r"“\1”", text)
    # volta aspas dentro das tags
    text = re.sub("§¢¬", '"', text)
    return text


def conserta_apostrofo(text: str) -> str:
    return re.sub(r"(\w+)´(\w+)", r"\1’\2", text)


def conserta_aspas_simples(text: str) -> str:
    # ʽ ʼ
    return text


def conserta_reticencias(text: str) -> str:
    return text.replace("...", "…")


def faz_correcoes_gerais(text) -> str:
    text = substitui_travessao(text)
    text = conserta_aspas(text)
    text = conserta_reticencias(text)
    text = conserta_apostrofo(text)
    # arq = str(filename)
    # if "variashistorias" in arq:
    #     text = text.replace("CAPÍTULO PRIMEIRO", "I").replace(
    #         "toda a casta de pombos", "toda a casta de pomos"
    #     )  # errada na edição
    # elif "Papeisavulsos" in arq:
    #     pass
    return text


roman_RE = re.compile(r"[IVXLC]+\b")


def palavra_titulo(palavra: str) -> str:

    if roman_RE.match(palavra.upper()):
        return palavra.upper()
    elif (
        len(palavra) <= 2
        and palavra not in ["Eu"]
        or palavra.lower()
        in ["sem", "das", "dos", "que", "quem", "desta", "deste", "esta", "este"]
    ):
        return palavra.lower()

    return palavra


def capitaliza(text: str) -> str:
    text = text.title()
    s = []
    for i in text.split():
        s.append(palavra_titulo(i))
    final_text = " ".join(s)
    if text.endswith(" "):
        final_text += " "
    return final_text


def capitaliza_soup(soup: Tag, primeiro=True) -> Tag:
    for el in soup.contents:
        if el.name == "script":
            continue
        if type(el) is NavigableString:
            txt = capitaliza(str(el))
            if primeiro and txt:
                txt = txt[0].upper() + txt[1:]
                primeiro = False

            el.replace_with(txt)
        elif not isinstance(el, Comment):
            capitaliza_soup(el, primeiro)
    return soup


if __name__ == "__main__":
    arquivos = Path("livros/www.machadodeassis.net/hiperTx_romances/obras/").glob(
        "tx_*htm"
    )
    arquivos0 = map(
        Path,
        [
            "livros/www.machadodeassis.net/hiperTx_romances/obras/tx_brascubas.htm",
            "livros/www.machadodeassis.net/hiperTx_romances/obras/tx_paginasrecolhidas.htm",
            "livros/www.machadodeassis.net/hiperTx_romances/obras/tx_historiasdameianoite.htm",
            "livros/www.machadodeassis.net/hiperTx_romances/obras/tx_Papeisavulsos.htm",
            "livros/www.machadodeassis.net/hiperTx_romances/obras/tx_Historiassemdata.htm",
            "livros/www.machadodeassis.net/hiperTx_romances/obras/tx_variashistorias.htm",
        ],
    )
    for arq in arquivos:
        if (
            "ContosFluminense" in str(arq)
            or "quincasborbaaestacao" in str(arq)
            or "tx_contosavulsos" in str(arq)
        ):
            continue
        try:
            print(f"§ Convertendo {arq}")
            processa(arq)
        except AssertionError as e:
            print(f"falhou {arq}, {e}")
