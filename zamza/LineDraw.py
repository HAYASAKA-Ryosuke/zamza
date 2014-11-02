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

    def _gridnum(self,xsmall,ysmall,xlarge,ylarge):
        res = []
        for i in range(0,self.__gridseparatenum(ylarge-ysmall)+1):
            x = []
            for j in range(0,self.__gridseparatenum(xlarge-xsmall)+1):
                x.append((xsmall+(self.space * j), ysmall+(self.space * i),))
            res.append(x)
        return res

    def gridnumlist(self, start=[], stop=[]):
        if start[0] <= stop[0] and start[1] < stop[1]:
            return self._gridnum(start[0], start[1], stop[0], stop[1])
        elif start[0] >= stop[0] and start[1] < stop[1]:
            return self._gridnum(stop[0], start[1], start[0], stop[1])
        elif start[0] <= stop[0] and start[1] > stop[1]:
            return self._gridnum(start[0], stop[1], stop[0], start[1])
        elif start[0] >= stop[0] and start[1] > stop[1]:
            return self._gridnum(stop[0], stop[1], start[0], start[1])

    def __gridseparatenum(self, pixel):
        return round(pixel/self.space)

