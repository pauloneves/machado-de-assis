# coding=utf-8

from ebooklib import epub


if __name__ == "__main__":
    book = epub.EpubBook()

    # add metadata
    # set metadata
    book.set_identifier("id123456")
    book.set_title("Sample book")
    book.set_language("pt-br")

    book.add_author("Author Authorowski")
    book.add_author(
        "Danko Bananko", file_as="Gospodin Danko Bananko", role="ill", uid="coauthor"
    )

    # intro chapter

    c1 = epub.EpubHtml(title="Introduction", file_name="intro.xhtml", lang="pt-br")
    c1.content = """<h1>Intro heading</h1><p>Farei aqui um footnote</p>
    <p>This footnote example uses the aside element with the epub:type attribute and bi-directional 
    hyperlinks.<sup><a id="source" href="chap_02.xhtml#ft-1-1" epub:type="noteref">1</a></sup></p>

    <p>This footnote example uses the aside element with the epub:type attribute and bi-directional 
    hyperlinks.<sup><a id="source2" href="#ft-1-2" epub:type="noteref">2</a></sup></p>

    <mbp:pagebreak />
    <mbp:section> 
    <span epub:type="pagebreak" id="footnotes" />
    <aside id="ft-1-2" epub:type="footnote">

    <p><a epub:type="noteref" href="#source2">2.</a> texto da nota de pé de página.</p>
    <p>será que rola ter vários parágrafos?
    <a href="#source2" style="font-size:2em">☚</a></p>

    </aside> 
    <mbp:section /> 
    """

    c2 = epub.EpubHtml(title="Footnotes", file_name="chap_02.xhtml", lang="pt-br")
    c2.content = """<h1>Referências</h1>
    <aside id="ft-1-1" epub:type="footnote">

    <p><a epub:type="noteref" href="intro.xhtml#source">1.</a> This is the footnote text, 
    which should be placed at the end of the chapter or book.
    <a href="intro.xhtml#source" style="font-size:2em">☚</a></p>

    </aside> 
    """

    # add chapters to the book
    book.add_item(c1)
    book.add_item(c2)

    # create table of contents
    # - add section
    # - add auto created links to chapters

    # book.toc = (
    #     epub.Link("intro.xhtml", "Introduction", "intro"),
    #     (epub.Section("Languages"), (c1, c2)),
    # )
    book.toc = (
        c1,
        c2,
    )

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
    book.spine = ["nav", c1, c2]

    # create epub file
    epub.write_epub("kindle/test.epub", book, {})
