'''
Provides some helped functions
'''

from PIL import Image, ImageFont, ImageDraw
import math


def draw_text(
    img: Image,
    text: str,
    location: tuple = (0, 0),
    text_color=(0, 0, 0)
) -> Image:
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 20)
    draw.text(location, text, font=font, fill=text_color)
    return img


def floating_judge(a, b, tol=1e-6):
    assert len(a) == len(b), "Length of the output and answer does not match"
    for i in range(len(a)):
        if not math.isclose(a[i], b[i], rel_tol=tol):
            return False
    return True
