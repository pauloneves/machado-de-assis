# /bin/env python

from bs4 import BeautifulSoup, Comment
import re
from pathlib import Path


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
        del secao["lang"]
        div_inicial = secao.parent.parent.parent.parent
        div_inicial.replace_with(secao)

        header = titulo.find_next("p")
        header.name = "h2"
        # header.text = header.text.strip()
        # header.string = header.string.strip()
        del header.attrs["align"]
        secao.insert_before(pg_break(livro))


def ajusta_titulos_capitulos(livro):
    pass


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


def cria_toc(livro):
    pass


def processa_livro(filename):
    livro = get_livro(filename)
    ajusta_titulo_livro(livro)
    ajusta_titulos_contos(livro)
    reorganiza_notas(livro)
    p = Path("kindle")
    p.mkdir(exist_ok=True)
    p = p / (get_nome_livro(livro) + ".html")
    with open(p, "w", encoding="utf8") as f:
        f.write(livro.prettify())


if __name__ == "__main__":
    processa_livro("livros/Papéis avulsos_files/tx_Papeisavulsos.html")
