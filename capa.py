"""
https://kdp.amazon.com/en_US/help/topic/G200645690

- jpg ou tiff
-  	Ideal dimensions for cover files are 2,560 pixels in height x 1,600 pixels in width.
- compressão mínima
- 72 dpi
- less than 50MB. 
- images should have a minimum resolution of 300 PPI (pixels per inch).
- Cover art with white or very light backgrounds can seem to disappear against the white background. Try adding a narrow (3-4 pixel) border in medium gray to define the boundaries of the cover.


Origem imagens:
https://commons.wikimedia.org/wiki/File:MarcFerrez_MachadodeAssis.jpg
https://commons.wikimedia.org/wiki/File:Assinatura_de_Machado_de_Assis.png
https://commons.wikimedia.org/wiki/File:Machado_de_Assis,_sem_data.tif

"""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance


def gera_capa(titulo="Várias Histórias"):
    # d8223a
    # Yeseva One
    # 140

    with Image.open("capa/capa-template.jpg") as img:
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(0.6)
        fnt = ImageFont.truetype("capa/YesevaOne-Regular.ttf", 220)
        d = ImageDraw.Draw(img)
        d.text((516, 1750), "\n".join(titulo.split()), fill="#d8223a", font=fnt)
        nome = f"kindle/{titulo}.jpg"
        img.save(nome, subsampling=0, quality=100)
    return nome
