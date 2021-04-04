# /bin/env python

from bs4 import BeautifulSoup, Comment
import re
from pathlib import Path
from ebooklib import epub
import slugify


def get_livro(filename="livros/Papéis avulsos_files/tx_Papeisavulsos.html"):
    with open(filename, encoding="cp1252") as f:
        livro = BeautifulSoup(f, "html.parser")
    return livro


def find_titulo_contos(text):
    return isinstance(text, Comment) and text.strip().startswith("*******")


def get_nome_livro(livro) -> str:
    return livro.title.string


def ajusta_titulo_livro(livro):
    titulo = get_nome_livro(livro)
    p = livro.find("p")
    p.name = "h1"
    del p.attrs["align"]
    autor = p.find_next("p")
    del autor.attrs["align"]
    notas = autor.find_next("p")
    notas.name = "h2"
    del notas.attrs["align"]


def pg_break(b):
    return b.new_tag(name="mpb:pagebreak")


def ajusta_titulos_contos(livro):
    """Títulos dos contos viram <H2>
    limpa excesso de divs
    """
    comentarios_titulo = livro.find_all(text=find_titulo_contos)

    for titulo in comentarios_titulo:
        secao = titulo.find_next("div", {"class": "section"})
        ajusta_secao(secao)

        header = titulo.find_next("p")
        header.name = "h2"
        # header.text = header.text.strip()
        # header.string = header.string.strip()
        del header.attrs["align"]
        secao.insert_before(pg_break(livro))


def ajusta_secao(secao):
    del secao["lang"]
    div_inicial = secao.parent.parent.parent.parent
    if div_inicial:
        div_inicial.replace_with(secao)


def ajusta_titulos_capitulos(livro):
    for secao in livro.find_all("div", {"class": "section"}):
        p = secao.find_all("p")
        # capítulo começa com 2 parágrafos centralizados
        if (
            len(p) > 1
            and p[0].attrs.get("align") == "center"
            and p[1].attrs.get("align") == "center"
        ):
            ajusta_secao(secao)
            secao.attrs["class"] = "subsection"

            h3 = livro.new_tag("h3")
            h3.append(p[0].b)
            h3.append(livro.new_tag("br"))
            for i in p[1].b.children:
                h3.append(i)
            secao.insert(0, h3)
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
    attrs["href"] = f"#{attrs['id']}"
    attrs["id"] = f"orig_{attrs['id']}"
    attrs["epub:type"] = "noteref"
    del attrs["onclick"]


def ajusta_todas_referencias(livro: BeautifulSoup):
    for a in livro.find_all("a", href="#"):
        ajusta_referencia(a)


def append_notas(livro: BeautifulSoup, notas: dict):
    h2 = livro.new_tag("h2")
    h2.append("Notas")
    livro.body.append(pg_break(livro))
    livro.body.append(h2)
    for nota, texto in notas.items():
        note = livro.new_tag("aside", id=nota, **{"epub:type": "footnote"})
        refback = livro.new_tag("a", href=f"#orig_{nota}", style="font-size:2em")
        refback.append("☚")
        note.append(BeautifulSoup(texto, "html.parser"))
        note.append(refback)
        livro.body.append(note)


def reorganiza_notas(livro):
    assert len(livro.find_all("h2")) > 0, "Primeiro tem que chamar 'ajusta_titulos'"

    notas = get_notas_dict(livro)
    ajusta_todas_referencias(livro)
    append_notas(livro, notas)


def prepara_toc(livro):
    toc = []
    for conto_num, h2 in enumerate(livro.find_all("h2")):
        h2.id = conto_num
        capitulos = []
        toc.append((str(conto_num), h2.string, capitulos))
        # usando fato que está sempre dentro de um div class=section
        for cap_num, h3 in enumerate(h2.parent.find_all("h3")):
            h3.id = f"{conto_num}.{cap_num}"
            capitulos.append((h3.id, h3.string))
    return toc


def cria_toc(livro, nome_arq):
    toc = prepara_toc(livro)

    livro.style.append(
        """
        div.chapter { margin-left: 1em}
        div.subchapter { margin-left: 2em} 
    """
    )
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


def processa_livro(filename="livros/Papéis avulsos_files/tx_Papeisavulsos.html"):
    livro = get_livro(filename)
    ajusta_titulo_livro(livro)
    ajusta_titulos_contos(livro)
    ajusta_titulos_capitulos(livro)
    reorganiza_notas(livro)
    return livro
    # cria_toc(livro)

    # p = Path("kindle")
    # p.mkdir(exist_ok=True)
    # p = p / (get_nome_livro(livro) + ".html")
    # with open(p, "w", encoding="utf8") as f:
    #     f.write(livro.prettify())


def gera_ebook(livro):
    book = epub.EpubBook()
    book.set_identifier("22061970ani")
    book.set_title(livro.h1.text)
    book.set_language("pt-br")

    book.add_author("Machado de Assis")

    capitulos = []
    for section in livro.find_all("div", {"class": "section"}):
        capitulo = epub.EpubHtml(
            title=section.h2.text,
            file_name=slugify.slugify(f"{section.id} {section.h2.text}"),
        )
        capitulo.content = str(section)
        capitulos.append(capitulo)
        book.add_item(capitulo)

    # create table of contents
    book.toc = capitulos

    # add navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # define css style
    style = """
@namespace epub "http://www.idpf.org/2007/ops";

body {
    font-family: Cambria, Liberation Serif, Bitstream Vera Serif, Georgia, Times, Times New Roman, serif;
}

h2 {
     text-align: left;
     text-transform: uppercase;
     font-weight: 200;     
}

ol {
        list-style-type: none;
}

ol > li:first-child {
        margin-top: 0.3em;
}


nav[epub|type~='toc'] > ol > li > ol  {
    list-style-type:square;
}


nav[epub|type~='toc'] > ol > li > ol > li {
        margin-top: 0.3em;
}

"""

    # add css file
    nav_css = epub.EpubItem(
        uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style
    )
    book.add_item(nav_css)

    # create spine
    book.spine = ["nav"] + capitulos

    # create epub file
    epub.write_epub(f"kindle/{livro.h1.text}.epub", book)


def processa():
    livro = processa_livro("livros/Papéis avulsos_files/tx_Papeisavulsos.html")
    gera_ebook(livro)


if __name__ == "__main__":
    processa()
