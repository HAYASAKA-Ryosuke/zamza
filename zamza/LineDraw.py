#!coding:utf-8
from PIL import ImageDraw, Image, ImageFont
import math

class LineDraw(object):
    def __init__(self):
        self.space = 10
        self.startx = None
        self.starty = None
        self.stopx = None
        self.stopy = None

    def gridnumlist(self, start, stop):
        res = []
        if start <= stop:
            res.append(start)
            res.extend([start+(val*self.space) for val in range(1, self.__gridseparatenum(stop-start))])
            res.append(stop)
        else:
            res.append(stop)
            res.extend([stop-(val*self.space) for val in range(1, self.__gridseparatenum(start-stop))])
            res.append(start)
        return res


    def __gridseparatenum(self, pixel):
        return round(pixel/self.space)

