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
    comentarios_titulo = livro.find_all(text=find_titulo_contos)
    for titulo in comentarios_titulo:
        header = titulo.find_next("p")
        header.name = "h2"
        # header.text = header.text.strip()
        # header.string = header.string.strip()
        header.attrs["style"] = "page-break-before:always"  # será que tem ser style?
        del header.attrs["align"]
        header.insert_before(pg_break(livro))


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
        p = livro.new_tag("p", id=nota)
        refback = livro.new_tag("a", href=f"#orig_{nota}")
        refback.append("«")
        p.append(BeautifulSoup(texto, "html.parser"))
        p.append(refback)
        livro.body.append(p)


def reorganiza_notas(livro):
    assert len(livro.find_all("h2")) > 0, "Primeiro tem que chamar 'ajusta_titulos'"

    notas = get_notas_dict(livro)
    ajusta_todas_referencias(livro)
    append_notas(livro, notas)


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
