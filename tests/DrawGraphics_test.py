#!coding:utf-8

import sys
sys.path.append('zamza')

import DrawGraphics

x = 3
y = 3
width = 100
height = 100
ic = DrawGraphics.ICdraw()
#ic.draw(x,y,width,height)
ic.pin()
ic.contour(x,y,width,height)

ic.show()

