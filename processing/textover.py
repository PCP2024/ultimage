import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont

def textover(image, text, left, top, color='#ffffff', fsize=15):
    if color is None:
        color = '#ffffff'
    if fsize is None:
        fsize = 15

    if (isinstance(image, numpy.ndarray)): 
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(image) 
        fontStyle = ImageFont.truetype( "./resources/impact.ttf", fsize, encoding="utf-8") 
        draw.text((left, top), text, color, font=fontStyle)
        return cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)