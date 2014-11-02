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


    def gridnumlist(self, start=[], stop=[]):
        res = []
        if start[0] <= stop[0] and start[1] < stop[1]:
                for i in range(0,self.__gridseparatenum(stop[1]-start[1])+1):
                    x = []
                    for j in range(0,self.__gridseparatenum(stop[0]-start[0])+1):
                        x.append((start[0]+(self.space * j), start[1]+(self.space * i),))
                    res.append(x)
        elif start[0] >= stop[0] and start[1] < stop[1]:
                for i in range(0,self.__gridseparatenum(stop[1]-start[1])+1):
                    x = []
                    for j in range(0,self.__gridseparatenum(start[0]-stop[0])+1):
                        x.append((stop[0]+(self.space * j), start[1]+(self.space * i),))
                    res.append(x)
        elif start[0] <= stop[0] and start[1] > stop[1]:
                for i in range(0,self.__gridseparatenum(start[1]-stop[1])+1):
                    x = []
                    for j in range(0,self.__gridseparatenum(stop[0]-start[0])+1):
                        x.append((start[0]+(self.space * j), stop[1]+(self.space * i),))
                    res.append(x)
        elif start[0] >= stop[0] and start[1] > stop[1]:
                for i in range(0,self.__gridseparatenum(start[1]-stop[1])+1):
                    x = []
                    for j in range(0,self.__gridseparatenum(start[0]-stop[0])+1):
                        x.append((stop[0]+(self.space * j), stop[1]+(self.space * i),))
                    res.append(x)
        return res

    def __gridseparatenum(self, pixel):
        return round(pixel/self.space)

