import machado
import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def livro():
    return machado.get_livro("livros/Papéis avulsos_files/tx_Papeisavulsos.html")


def book(txt):
    return BeautifulSoup(f"<html><body>{txt}</body></html>", "html.parser")


# def test_ajusta_capitulos(livro):
#     b = book(
#         """<!-- Inicio CAPITULO I -->

# <p align="center"><b>O ALIENISTA <a href="#" id="mynewanchorOA*" onclick="return false;"> * </a></b>
# """
#     )
#     machado.ajusta_capitulos(livro)


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

    machado.ajusta_titulos_contos(b)
    assert len(b.find_all("div")) == 2, "tem que remover divs"
    assert b.h2, "títulos dos contos deveriam ser substituídos por H2"
    assert b.h2.text.lower().startswith("o empréstimo")
    secao = b.find("div", {"class": "section"})
    assert secao.previous_sibling.name.startswith("mpb")
    assert not b.find_all(lambda tag: "lang" in tag.attrs)


def test_ajusta_inicio_capitulos():
    b = book(
        """
        <div class="espacoToptHTX"><a name="OAXIII">&nbsp;</a></div>

    <div id="shadow-container">
            <div class="shadow1">
                <div class="shadow2">
                    <div class="shadow3">
                        <div class="section" lang="de">
    <!-- Inicio CAPITULO XIII -->

    <p align="center"><b>XIII</b></p> <br>
    <p align="center"><b><i><a href="#" id="mynewanchorOA74" onclick="return false;">Plus ultra</a></i>!</b>

    """
    )

    machado.ajusta_titulos_capitulos(b)
    print(b)
    assert b.h3
    assert "XIII" in b.h3.text
    assert "Plus ultra" in b.h3.text
    subsection = b.find("div", {"class": "subsection"})
    assert subsection
    assert "lang" not in subsection.attrs


def test_ajusta_inicio_capitulos_com_conto():
    b = book(
        """
        <div class="espacoToptHTX"><a name="OAXIII">&nbsp;</a></div>

    <div id="shadow-container">
            <div class="shadow1">
                <div class="shadow2">
                    <div class="shadow3">
                        <div class="section" lang="de">
    <!-- Inicio CAPITULO XIII -->

    <p align="center"><b>XIII</b></p> <br>
    <p align="center"><b><i><a href="#" id="mynewanchorOA74" onclick="return false;">Plus ultra</a></i>!</b>

    <!-- *********************************** O EMPRESTIMO  ****************************************************** -->
    </div></div></div></div></div>

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

    machado.ajusta_titulos_capitulos(b)
    assert b.h3
    assert len(b.find_all("h3")) == 1


def test_ajusta_titulos_ordem_correta():
    b = book(
        """
    <!-- ****************************************    O ALIENISTA  ***************************************************-->

<div class="espacoToptHTX"><a name="OAI">&nbsp;</a></div>


<div id="shadow-container">
		<div class="shadow1">
			<div class="shadow2">
				<div class="shadow3">
				  <div class="section" lang="de">
<!-- Inicio CAPITULO I -->

<p align="center"><b>O ALIENISTA <a href="#" id="mynewanchorOA*" onclick="return false;"> * </a></b>

</p> <br>
<p align="center"><b>CAPÍTULO PRIMEIRO</b> </p> <br>
<p align="center"><b>De como <a href="#" id="mynewanchorOA1" onclick="return false;">Itaguaí</a> ganhou uma casa de orates</b>

"""
    )
    machado.ajusta_titulos_contos(b)
    machado.ajusta_titulos_capitulos(b)

    assert b.h2.text.startswith("O ALIENISTA")

    assert b.h2.find_next("h3"), "h3 deve vir depois do h2"
    assert b.h2.find_next("h3").text.startswith("CAPÍTULO")


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
    id_, texto = machado.parse_nota(nota)
    assert "mynewanchorVT42" == id_
    assert 'A "capital"' == texto


def test_get_notas_dict(livro):
    notas_dict = machado.get_notas_dict(livro)
    assert "mynewanchorVT42" in notas_dict


def test_ajusta_referencia():
    ref = BeautifulSoup(
        '<a href="#" id="mynewanchorNTA1" onclick="return false;">texto</a>',
        "html.parser",
    ).find("a")
    machado.ajusta_referencia(ref)
    assert ref.attrs["href"].endswith("#mynewanchorNTA1"), ref
    assert ref.text == "texto"
    assert ref.attrs["id"] == "orig_mynewanchorNTA1"


def ajusta_todas_referencias():
    b = machado.get_book(
        """
        <a href="#" id="mynewanchor1" onclick="return false;">texto1</a>"
        <a href="#" id="mynewanchor2" onclick="return false;">texto2</a>"
        """
    )
    machado.ajusta_todas_referencias(b)
    for a in b.find_all("a"):
        assert "onclick" not in a


def test_append_notas(livro):
    notas = {"nota1": "texto1", "nota2": "texto2"}
    assert len(livro.find_all("h2")) == 0, "Opa, achei que não tinha nada aqui"
    machado.append_notas(livro, notas)
    h2 = livro.find("h2")
    assert h2
    assert len(h2.find_all_next("aside")) == len(notas)


def test_cria_toc():
    b = book(
        """
        <div class="section">
            <h2>conto1</h2>
        </div>
        <div class="section">
            <h2>conto2</h2>
            <h3><b>capitulo1</b></h3>
        </div>
        <div class="subsection">
            <h3><b>capitulo2</b></h3>
        </div>
        <div class="subsection">
            <h3><b>capitulo3</b></h3>
        </div>
    """
    )
    toc = machado.prepara_toc(b)
    assert toc == [
        ("1", "conto1", []),
        (
            "2",
            "conto2",
            [
                ("2.1", "capitulo1"),
                ("2.2", "capitulo2"),
                ("2.3", "capitulo3"),
            ],
        ),
    ]

    for h2 in b.find_all("h2"):
        assert h2.attrs["id"]
    for h3 in b.find_all("h3"):
        assert h3.attrs["id"]
        assert "." in h3.attrs["id"]


def test_ajusta_titulos(livro):
    machado.ajusta_titulos(livro)
    assert (
        len(livro.find_all("div", lang="de")) == 0
    ), "todas seções com lang foram retiradas"


def test_processa_livro():
    machado.processa_livro()
    assert True, "Nenhuma exceção foi disparada"


def test_subtitulo():
    doc = BeautifulSoup(
        '<h3 id="2.1"><b>CAPÍTULO PRIMEIRO</b><br/>De como  ganhou uma casa de orates</h3> ',
        "html.parser",
    )
    st = machado.extrai_subtitulo(doc.h3)
    assert "De como  ganhou uma casa de orates" in st


def test_subtitulo_so_uma_linha():
    doc = BeautifulSoup(
        '<h3 id="1.1"><b>Advertência</b><br/></h3> ',
        "html.parser",
    )
    st = machado.extrai_subtitulo(doc.h3)
    assert st == "Advertência"


def test_subtitulo_com_tag():
    doc = BeautifulSoup(
        '<h3 id="2.13"><b>XIII</b><br/><b><i><a epub:type="noteref" href="notas.html#mynewanchorOA74" id="orig_mynewanchorOA74">Plus ultra</a></i>!</b></h3>',
        "html.parser",
    )
    st = machado.extrai_subtitulo(doc.h3)
    assert "Plus ultra !" in st


def test_ajusta_titulo_capitulo_terror():
    b = book(
        """					<div class="section" lang="de">
<!-- inicio capitulo V-->

<p align="center"><b>V</b></p> <br>
<p align="center"><b>O <a href="#" id="mynewanchorOA36" onclick="return false;">Terror</a></b>
"""
    )
    machado.ajusta_titulos_capitulos(b)
    assert "Terror" in b.h3.get_text()


def test_substitui_travessao():
    assert "dir-te" == machado.substitui_travessao("dir-te")
    assert "dir-te-ei" == machado.substitui_travessao("dir-te-ei")
    assert "<!-- FIM: capitulo-->" == machado.substitui_travessao(
        "<!-- FIM: capitulo-->"
    )

    assert '<p class="noindent">— fala' == machado.substitui_travessao("<p>- fala")
    assert "<p>ROMEU. — E que vos disseram eles? </p>" == machado.substitui_travessao(
        "<p>ROMEU. - E que vos disseram eles? </p>"
    )
    assert " — Morrer por ela? — disse eu. </p>" == machado.substitui_travessao(
        " - Morrer por ela? - disse eu. </p>"
    )
    assert "uma frase — disgressão — continua o tema" == machado.substitui_travessao(
        "uma frase - disgressão - continua o tema"
    )

    # linha nunca começa com apóstrofe, sempre tem um <p> antes
    assert (
        " — Tinha muito bom dado! — suspirou lentamente o vigário —."
        == machado.substitui_travessao(
            " - Tinha muito bom dado! - suspirou lentamente o vigário -."
        )
    )
    assert " — Mas, perdão — atalhei —," == machado.substitui_travessao(
        " - Mas, perdão — atalhei -,"
    )
    assert " — disse-me Capitu ao voltar da igreja —;" == machado.substitui_travessao(
        " - disse-me Capitu ao voltar da igreja -;"
    )


def test_conserta_aspas():
    assert "“a”" == machado.conserta_aspas('"a"')
    assert '<a href="x">' == machado.conserta_aspas('<a href="x">')
    assert '“a<a href="b">b</a>”' == machado.conserta_aspas('"a<a href="b">b</a>"')
