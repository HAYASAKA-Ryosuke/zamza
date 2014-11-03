#!coding:utf-8
from PIL import ImageDraw, Image, ImageFont
import os
import ICDraw
import LineDraw


class draw(ICDraw.ICDraw, LineDraw.Linedraw):
    def __init__(self):
        self.im = Image.new('RGBA', (780, 780), (128, 128, 128, 0))
        self.drawline = ImageDraw.Draw(self.im)
        self.font = ImageFont.truetype(os.path.dirname(__file__) + "/../font/ipaexg.ttf", size=16)
        ICDraw.ICDraw.__init__(self)
        LineDraw.Linedraw.__init__(self)

    def show(self):
        self.im.show()
