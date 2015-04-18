#!coding:utf-8
from PIL import ImageDraw, Image, ImageFont
import os
from ic import IC
from line_draw import LineDraw


class Draw(IC, LineDraw):
    def __init__(self):
        self.im = Image.new('RGBA', (780, 780), (255, 255, 255, 255))
        self.draw_line = ImageDraw.Draw(self.im)
        self.font = ImageFont.truetype(os.path.dirname(__file__) + "/../font/ipaexg.ttf", size=16)
        IC.__init__(self)
        LineDraw.__init__(self)

    def show(self):
        self.im.show()
