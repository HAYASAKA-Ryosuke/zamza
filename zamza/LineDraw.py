#!coding:utf-8
from PIL import ImageDraw, Image, ImageFont
import math

class LineDraw(object):
    def __init__(self):
        self.startx = None
        self.starty = None
        self.stopx = None
        self.stopy = None

    def gridnum(self, pixel):
        return round(pixel/10)

