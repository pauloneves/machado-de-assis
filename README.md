# Origem dos arquivos

<http://www.machadodeassis.net/hiperTx_romances/obras/papeisavulsos.htm>

## Características do html

- tudo dividido em parágrafos direitinho
- as notas são tags \<a\> no código que referencia a partir do atributo id do a
- [dicas de como preparar html](https://www.aliciaramirez.com/2014/05/how-to-make-a-kindle-ebook-from-scratch/)

## TODO

- [ ] capítulo 0, advertência, está sumido
- [ ] subseções na toc
- [ ] tirar sublinhado toc
- [ ] o alienista e notas como capítulos
- [ ] links de volta das notas não funcionam (será que incluo as notas no próprio capítulo?)
- [ ] fru fru na formatação
- [x] referencias para toc
- [x] ajustar TOC
- [x] espacoToptHTX -> antes com **** são inícios do conto, antes div é capítulo. 5 divs seguintes é falso
- [x] tirar os divs em cada capítulo
- [x] considere matar o style inicial
- [x] tirar background color
- [x] colocar footnotes no fim de cada capítulo
- [x] [formatar footnotes](https://kdp.amazon.com/en_US/help/topic/GH4DRT75GWWAGBTU#footnote_guideline)


## Entendo estado atual

espacotopHTX > section > h1 Papeis avulsos (sem id)
                       > h2 Nota desta edição  (id 0)

subsection > h3 Advertência (sem id)

Aqui temos um problema maior: vem o comentário do título do livro, depois h3#1.0 (capítulo primeiro) e então vem o h2#O ALIENISTA

subsection > h3 (sem id) capítulo II

todos os capítulos vêm bonitinhos, com h3 mas sem ID

section > h2#2

subsection > Aqui pego outro erro, vem o comentário do título do capítulo, um h3#4.0 e então um h2#4 NA ARCA



## Publicação final

- usar Calibre e exportar para KFX
