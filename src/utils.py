'''
Provides some helped functions
'''

from PIL import Image, ImageFont, ImageDraw


def draw_text(
    img: Image,
    text: str,
    location: tuple = (0, 0),
    text_color=(0, 0, 0)
) -> Image:
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 20)
    draw.text(location, text, font=font, fill=text_color)
    return img
