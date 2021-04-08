# /bin/env python

from bs4 import BeautifulSoup, Comment
import re
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

    section = livro.find("div", {"class": "section"})
    del section.attrs["lang"]


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

        header = titulo.find_next("p")
        header.name = "h2"
        # header.text = header.text.strip()
        # header.string = header.string.strip()
        del header.attrs["align"]
        secao.insert_before(pg_break(livro))


def ajusta_secao(secao: BeautifulSoup, subsection=False):
    del secao["lang"]
    div_inicial = secao.parent.parent.parent.parent
    if div_inicial:
        div_inicial.replace_with(secao)
        if subsection:
            secao.attrs["class"] = "subsection"


def ajusta_titulos_capitulos(livro: BeautifulSoup):
    for secao in livro.find_all("div", {"class": "section"}):
        p = secao.find_all("p")
        # capítulo começa com 2 parágrafos centralizados
        if (
            len(p) > 1
            and p[0].attrs.get("align") == "center"
            and p[1].attrs.get("align") == "center"
        ):
            ajusta_secao(secao, subsection=True)

            h3 = livro.new_tag("h3")
            h3.append(p[0].b)
            h3.append(livro.new_tag("br"))
            for i in p[1].b.children:
                h3.append(i)
            p[0].insert_before(h3)
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


def append_notas(livro: BeautifulSoup, notas: dict):
    section = livro.new_tag("div")
    section.attrs["class"] = "section"
    h2 = livro.new_tag("h2")
    h2.append("Notas")
    section.append(h2)
    livro.body.append(pg_break(livro))
    for nota, texto in notas.items():
        note = livro.new_tag("aside", id=nota, **{"epub:type": "footnote"})
        refback = livro.new_tag("a", href=f"#orig_{nota}", style="font-size:2em")
        refback.append("☚")
        note.append(BeautifulSoup(texto, "html.parser"))
        note.append(refback)
        section.append(note)
    livro.body.append(section)


def reorganiza_notas(livro):
    assert len(livro.find_all("h2")) > 0, "Primeiro tem que chamar 'ajusta_titulos'"

    notas = get_notas_dict(livro)
    ajusta_todas_referencias(livro)
    append_notas(livro, notas)


def prepara_toc(livro):
    toc = []
    for conto_num, h2 in enumerate(livro.find_all("h2")):
        h2.attrs["id"] = str(conto_num)
        capitulos = []
        toc.append((str(conto_num), h2.string, capitulos))
        # usando fato que está sempre dentro de um div class=section
        for cap_num, h3 in enumerate(h2.parent.find_all("h3")):
            h3.attrs["id"] = f"{conto_num}.{cap_num}"
            capitulos.append((h3.attrs["id"], h3.string))
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
    ajusta_titulos(livro)
    reorganiza_notas(livro)
    prepara_toc(livro)
    return livro


def ajusta_titulos(livro):
    ajusta_titulo_livro(livro)
    ajusta_titulos_contos(livro)
    ajusta_titulos_capitulos(livro)

    assert not len(
        livro.find_all("div", {"class": "section", "lang": "de"})
    ), "depois de ajustar todos os títulos não pode sobrar seções"


def gera_ebook(livro):
    book = epub.EpubBook()
    book.set_identifier("22061970ni")
    book.set_title(livro.h1.text)
    book.set_language("pt-br")

    book.add_author("Machado de Assis")

    capitulos = []
    toc = []
    pos = 1
    for section in livro.find_all("div", {"class": "section"}):
        print(pos, section.h2.text)
        print(section.h3.text if section.h3 else "nada")
        pos += 1
        capitulo = epub.EpubHtml(
            title=section.h2.text.strip(" \n*"),
            file_name=slugify.slugify(section.h2.text) + ".html",
            media_type="text/html",
        )
        capitulo.set_content(str(section))
        capitulos.append(capitulo)

        sub_capitulos = [
            f"{capitulo.filename}#{h3.attrs['id']}" for h3 in section.find_all("h3")
        ]
        print(sub_capitulos)
        book.add_item(capitulo)
        toc.append(
            (epub.Section(title=capitulo.title, href=capitulo.file_name), sub_capitulos)
        )

    # (epub.Link('chap_01.xhtml', 'Introduction', 'intro'),
    #              (epub.Section('Simple book'),
    #              (c1, ))
    #             )
    # create table of contents
    book.toc = toc
    # (
    #     (epub.Section("seçao 1234"), capitulos[0:3]),
    #     # capitulos[3:5],
    #     (
    #         epub.Section(title="Title seção", href=capitulo.file_name),
    #         ["abc", "cde"],
    #     ),
    # )

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
     /*text-transform: uppercase;*/
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

nav[epub|type~='toc'] > a {
     text-decoration: none;
}
"""

    # add css file
    nav_css = epub.EpubItem(
        uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style
    )
    book.add_item(nav_css)

    # create spine
    book.spine = ["nav"]  # + capitulos

    # create epub file
    epub.write_epub(f"kindle/{livro.h1.text}.epub", book)


def processa():
    livro = processa_livro("livros/Papéis avulsos_files/tx_Papeisavulsos.html")
    with open("livro_alterado.html", "w") as file:
        file.write(str(livro))
    gera_ebook(livro)


if __name__ == "__main__":
    processa()
