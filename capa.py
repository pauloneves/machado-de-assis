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


Inspiração: 
https://www.nypl.org/blog/2014/09/03/generative-ebook-covers
http://www.lightindustry.org/simon_marker.jpg

"""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageOps

import re


def gera_capa(titulo="Várias Histórias"):
    # d8223a
    # Yeseva One
    # 140

    with Image.open("capa/capa-template.jpg") as img:
        color_img = ImageOps.colorize(img.convert("L"), black="black", white="#575b81")
        brightness_enhancer = ImageEnhance.Brightness(color_img)
        img = brightness_enhancer.enhance(0.9)
        fnt = ImageFont.truetype("capa/YesevaOne-Regular.ttf", 220)
        d = ImageDraw.Draw(img)
        d.text((50, 1750), "\n".join(titulo.upper().split()), fill="#d9c347", font=fnt)
        nome = f"kindle/{titulo}.jpg"
        img.save(nome, subsampling=0, quality=100)
    return nome
