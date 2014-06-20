#!coding:utf-8
from PIL import ImageDraw, Image


class ICdraw(object):
    def __init__(self):
        self.im = Image.new('RGB', (100, 100), 'rgb(128,128,128)')
        self.draw = ImageDraw.Draw(self.im)

    def drawIC(self, *args):
        self.line(((0, 0), (50, 50), (80, 20)), fill='rgb(255, 0, 0)')


class Import(object):
    def __init__(self):
        pass
