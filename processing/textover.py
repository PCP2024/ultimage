import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont
from configuration.config import load_defaults


def textover(image, text, coords, color='#ffffff', fsize=15):
    defaults = load_defaults()
    font = defaults['default_font']
    if coords == (None, None):
        coords = defaults['coordinates']
    if color is None:
        color = defaults['color']
    if fsize is None:
        fsize = defaults['size']
    left, top = coords
    

    if (isinstance(image, numpy.ndarray)): 
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(image) 
        fontStyle = ImageFont.truetype( font['font'], fsize, encoding="utf-8") 
        draw.text((left, top), text, color, font=fontStyle)
        return cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)