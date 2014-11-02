#!coding:utf-8
from PIL import ImageDraw, Image, ImageFont
import os
import ICDraw


class draw(ICDraw.ICdraw):
    def __init__(self):
        self.icname = {}
        self.im = Image.new('RGBA', (480, 780), (128, 128, 128, 0))
        self.drawline = ImageDraw.Draw(self.im)
        self.font = ImageFont.truetype(os.path.dirname(__file__) + "/../font/ipaexg.ttf", size=16)
        self.widthmargin = self.leftmargin + self.rightmargin
        self.heightmargin = self.topmargin + self.bottommargin
        self.toppinpos = []
        self.rightpinpos = []
        self.leftpinpos = []
        self.bottompinpos = []


    def show(self):
        self.im.show()
