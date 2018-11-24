'''
Provides some helped functions
'''

from PIL import Image, ImageFont, ImageDraw


def draw_text(
    img: Image,
    text: str,
    location: tuple = (0, 0)
) -> Image:
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text(location, text, font=font)
    return img
