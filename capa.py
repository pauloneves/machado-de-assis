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

import textwrap

from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps

colors = [
    "#46bcde",
    "#52d273",
    "#e94f64",
    "#e57254",
    "#e5c454",
    "#ffb901",
    "#e75064",
]


def gera_capa(titulo="Várias histórias", wrap=9, title_size=260):
    # d8223a
    # Yeseva One
    # 140
    def decrease_text(wrap, title_size):
        wrap = round(1.25 * wrap)
        title_size = round(title_size // 1.25)
        return wrap, title_size

    with Image.open("capa/capa-template.jpg") as img:
        # img = img.convert("L")
        # color_img = ImageOps.colorize(img, black="black", white="white")
        # brightness_enhancer = ImageEnhance.Brightness(color_img)
        # img = brightness_enhancer.enhance(1.2)
        font_name = "capa/YesevaOne-Regular.ttf"
        fnt_title = ImageFont.truetype(font_name, title_size)
        d = ImageDraw.Draw(img)
        titulo_wrap = "\n".join(
            textwrap.wrap(titulo.upper(), wrap, break_long_words=False)
        )
        title_pos = (50, 1700)

        text_width, text_height = d.textsize(titulo_wrap, font=fnt_title)
        if text_width + title_pos[0] > 1600 or text_height + title_pos[1] > 2500:
            wrap, title_size = decrease_text(wrap, title_size)
            return gera_capa(titulo, wrap, title_size)

        fnt_edicao = ImageFont.truetype(font_name, title_size // 3)
        d.text(
            (title_pos[0] + 15, title_pos[1] + text_height + 20),
            "edição comentada",
            fill="darkgray",
            font=fnt_edicao,
        )

        assinatura = "Machado de Assis"
        fnt_assinatura = ImageFont.truetype(font_name, title_size // 2)
        _, text_height = d.textsize(assinatura, font=fnt_assinatura)
        d.text(
            (title_pos[0] + 15, title_pos[1] - text_height),
            assinatura,
            fill="lightgray",
            font=fnt_assinatura,
        )
        this_color = colors[sum(ord(i) for i in titulo) % len(colors)]
        d.text(title_pos, titulo_wrap, fill=this_color, font=fnt_title)

        nome = f"kindle/{titulo}.jpg"
        img.save(nome, subsampling=0, quality=100)
    return nome


if __name__ == "__main__":
    gera_capa()