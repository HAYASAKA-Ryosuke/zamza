# coding:utf-8

import sys
sys.path.append('zamza')

import DrawGraphics
import unittest


class testDrawGraphics(unittest.TestCase):
    def setUp(self):
        x = 10
        y = 10
        self.ic = DrawGraphics.ICdraw()
        self.ic.pin(top=0, left=8, bottom=0, right=8)
        self.ic.text(top=[],
                left=["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
                bottom=[],
                right=["p9", "p10", "p11", "p12", "p13", "p14", "p15", "p16"]
                )
        self.ic.name("IC1")
        self.ic.draw(x, y)

        x = 300
        y = 300
        self.ic.pin(top=8, left=8, bottom=8, right=8)
        self.ic.text(top=["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
                left=["p9", "p10", "p12", "p13", "p14", "p15", "p16", "p17"],
                bottom=["p18", "p19", "p20", "p21", "p22", "p23", "p24", "p25"],
                right=["p26", "p27", "p28", "p29", "p30", "p31", "p32", "p33"]
                )
        self.ic.name("IC2")
        self.ic.draw(x, y)
        self.ic.show()

    def test_getpinpos(self):
        self.assertEqual(("top", 1, (366, 300)), self.ic.getpinpos("IC2", "p2"))
        self.assertEqual(("left", 2, (10, 82)), self.ic.getpinpos("IC2", "p12"))
        self.assertEqual(("right", 3, (70, 108)), self.ic.getpinpos("IC2", "p29"))
        self.assertEqual(("bottom", 4, (444, 538)), self.ic.getpinpos("IC2", "p22"))

unittest.main()
