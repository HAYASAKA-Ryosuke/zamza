#!coding:utf-8
from PIL import ImageDraw, Image, ImageFont
import os
import ICDraw
import LineDraw


class draw(ICDraw.ICdraw, LineDraw.Linedraw):
    def __init__(self):
        self.icname = {}
        self.im = Image.new('RGBA', (780, 780), (128, 128, 128, 0))
        self.drawline = ImageDraw.Draw(self.im)
        self.font = ImageFont.truetype(os.path.dirname(__file__) + "/../font/ipaexg.ttf", size=16)
        self.widthmargin = self.leftmargin + self.rightmargin
        self.heightmargin = self.topmargin + self.bottommargin
        self.toppinpos = []
        self.rightpinpos = []
        self.leftpinpos = []
        self.bottompinpos = []
        LineDraw.Linedraw.__init__(self)


    def show(self):
        self.im.show()
