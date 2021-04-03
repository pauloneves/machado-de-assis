import parse
import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def livro():
    return parse.get_livro("livros/Papéis avulsos_files/tx_Papeisavulsos.html")


def book(txt):
    return BeautifulSoup(f"<html><body>{txt}</body></html>", "html.parser")


# def test_ajusta_capitulos(livro):
#     b = book(
#         """<!-- Inicio CAPITULO I -->

# <p align="center"><b>O ALIENISTA <a href="#" id="mynewanchorOA*" onclick="return false;"> * </a></b>
# """
#     )
#     parse.ajusta_capitulos(livro)


# def test_ajusta_capitulos_2(livro):
#     b = book(
#         """<!-- Inicio CAPITULO II-->

# <p align="center"><b></b></p> <br>
# <p align="center"><b>CAPÍTULO B</b> </p> <br>"""
#     )


def test_ajusta_titulo_contos():
    b = book(
        """<!-- *********************************** O EMPRESTIMO  ****************************************************** -->


<div class="'espacoToptHTX'"><a name="OEI">&nbsp;</a></div>


<div id="shadow-container">
		<div class="shadow1">
			<div class="shadow2">
				<div class="shadow3">
				  <div class="section" lang="de">
<!-- Inicio CAPITULO I -->


<p align="center"><b>O EMPRÉSTIMO <a href="#" id="mynewanchorOE*" onclick="return false;"> * </a></b>
"""
    )

    parse.ajusta_titulos_contos(b)
    print(b)
    assert len(b.find_all("div")) == 2, "tem que remover divs"
    assert b.h2.text.lower().startswith("o empréstimo")
    secao = b.find("div", {"class": "section"})
    assert secao.previous_sibling.name.startswith("mpb")


# def test_remove_divs_inicio_contos():
#     b = book(
#         """<!-- *********************************** O EMPRESTIMO  ****************************************************** -->


# <div class="espacoToptHTX"><a name="OEI">&nbsp;</a></div>


# <div id="shadow-container">
# 		<div class="shadow1">
# 			<div class="shadow2">
# 				<div class="shadow3">
# 				  <div class="section" lang="de">
# <!-- Inicio CAPITULO I -->


# <p align="center"><b>O EMPRÉSTIMO <a href="#" id="mynewanchorOE*" onclick="return false;"> * </a></b>
# 					</div>
# 				</div>
# 			</div>
# 		</div>
# </div>
# """
#     )

#     parse.ajusta_titulos_contos(b)
#     assert len(b.find_all("div", recursive=True)) == 0


def test_parse_nota():
    nota = BeautifulSoup(
        """<script type="text/javascript">
        new HelpBalloon({
                title: '',
                content: 'A "capital"',
                icon: $('mynewanchorVT42'),
                useEvent: ['mouseover'],
        anchorPosition: 'top left',
                iconStyle: {
                        'cursor': 'pointer',
                        'verticalAlign': 'middle'
                }
        });
</script>""",
        "html.parser",
    )
    id_, texto = parse.parse_nota(nota)
    assert "mynewanchorVT42" == id_
    assert 'A "capital"' == texto


def test_get_notas_dict(livro):
    notas_dict = parse.get_notas_dict(livro)
    assert "mynewanchorVT42" in notas_dict


def test_ajusta_referencia():
    ref = BeautifulSoup(
        '<a href="#" id="mynewanchorNTA1" onclick="return false;">texto</a>',
        "html.parser",
    ).find("a")
    parse.ajusta_referencia(ref)
    assert ref.attrs["href"] == "#mynewanchorNTA1", ref
    assert ref.text == "texto"
    assert ref.attrs["id"] == "orig_mynewanchorNTA1"


def ajusta_todas_referencias():
    b = parse.get_book(
        """
        <a href="#" id="mynewanchor1" onclick="return false;">texto1</a>"
        <a href="#" id="mynewanchor2" onclick="return false;">texto2</a>"
        """
    )
    parse.ajusta_todas_referencias(b)
    for a in b.find_all("a"):
        assert "onclick" not in a


def test_append_notas(livro):
    notas = {"nota1": "texto1", "nota2": "texto2"}
    assert len(livro.find_all("h2")) == 0, "Opa, achei que não tinha nada aqui"
    parse.append_notas(livro, notas)
    h2 = livro.find("h2")
    assert h2
    assert len(h2.find_next_siblings("aside")) == len(notas)
    uma_nota = h2.find_next("aside")
    assert uma_nota.find("a").attrs["href"].startswith("#orig_"), uma_nota.attrs["href"]
