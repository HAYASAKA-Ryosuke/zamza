#!coding:utf-8
from PIL import ImageDraw, Image, ImageFont


class ICdraw:
    def __init__(self):
        self.im = Image.new('RGBA', (480, 780), (128,128,128,0))
        self.drawline = ImageDraw.Draw(self.im)
        self.font = ImageFont.truetype(size=12)

    def contour(self,x,y,width,height,color='black'):
        self.drawline.line(((x, y), (x, y+height), (x+width, y+height),(x+width, y),(x, y)), fill=color,width=2)

    def pin(self):
        self.drawline.text((5,5),"hello")

    def draw(self,one,two,three,four):
        self.pin()
        #self.contor()

    def show(self):
        self.im.show()

class Import(object):
    def __init__(self):
        pass

