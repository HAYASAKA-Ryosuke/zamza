# coding:utf-8

import sys
sys.path.append('zamza')

import DrawGraphics
import unittest

#x = 3
#y = 3
#width = 100
#height = 100
#ic = DrawGraphics.ICdraw()
##ic.draw(x,y,width,height)
#ic.pin()
#ic.contour(x, y, width, height)
#
#ic.show()


x = 3
y = 3
ic = DrawGraphics.ICdraw()
ic.pin(top=0, left=8, bottom=0, right=8)
ic.text(top=[],
        left=["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
        bottom=[],
        right=["p9", "p10", "p11", "p12", "p13", "p14", "p15", "p16"]
        )
ic.draw(x, y)
ic.show()
x = 3
y = 3
ic = DrawGraphics.ICdraw()
ic.pin(top=8, left=8, bottom=8, right=8)
ic.text(top=["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
        left=["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
        bottom=["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
        right=["p9", "p10", "p11", "p12", "p13", "p14", "p15", "p16"]
        )
ic.draw(x, y)
ic.show()
#class testDrawGraphics(unittest.TestCase):
#    def drawic(self):
#        x = 3
#        y = 3
#        ic = DrawGraphics.ICdraw()
#        ic.pin(top=0, left=8, bottom=0, right=8)
#        ic.text(top=[],
#                left=["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
#                bottom=[],
#                right=["p9", "p10", "p11", "p12", "p13", "p14", "p15", "p16"]
#                )
#        ic.draw(x, y)
#        ic.show()
#unittest.main()
