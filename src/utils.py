'''
Provides some helped functions
'''

import math

from PIL import Image, ImageFont, ImageDraw
from logging_config import logger


def draw_text(
    img: Image,
    text: str,
    location: tuple = (0, 0),
    text_color=(0, 0, 0)
) -> Image:
    draw = ImageDraw.Draw(img)

    try:
        # For Linux
        font = ImageFont.truetype("DejaVuSans.ttf", 20)
    except Exception as err:
        logger.warning(err, exc_info=True)
        # For others
        font = ImageFont.load_default()
    draw.text(location, text, font=font, fill=text_color)
    return img


def floating_judge(a, b, tol=1e-6):
    assert len(a) == len(b), "Length of the output and answer does not match"
    for i in range(len(a)):
        if not math.isclose(a[i], b[i], rel_tol=tol):
            return False
    return True
