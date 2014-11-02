# coding:utf-8

import sys
sys.path.append('zamza')

import DrawGraphics
import unittest


class testDrawGraphics(unittest.TestCase):
    def setUp(self):
        x = 10
        y = 10
        self.ic = DrawGraphics.draw()
        self.ic.ICpin(top=0, left=8, bottom=0, right=8)
        self.ic.ICtext(top=[],
                left=["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
                bottom=[],
                right=["p9", "p10", "p11", "p12", "p13", "p14", "p15", "p16"]
                )
        self.ic.ICname("IC1")
        self.ic.ICdraw(x, y)

        x = 300
        y = 300
        self.ic.ICpin(top=8, left=8, bottom=8, right=8)
        self.ic.ICtext(top=["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
                left=["p9", "p10", "p12", "p13", "p14", "p15", "p16", "p17"],
                bottom=["p18", "p19", "p20", "p21", "p22", "p23", "p24", "p25"],
                right=["p26", "p27", "p28", "p29", "p30", "p31", "p32", "p33"]
                )
        self.ic.ICname("IC2")
        self.ic.ICdraw(x, y)

    def test_getpinpos(self):
        self.assertEqual(("top", 1, (360, 300)), self.ic.ICgetpinpos("IC2", "p2"))
        self.assertEqual(("left", 2, (10, 70)), self.ic.ICgetpinpos("IC2", "p12"))
        self.assertEqual(("right", 3, (70, 90)), self.ic.ICgetpinpos("IC2", "p29"))
        self.assertEqual(("bottom", 4, (420, 490)), self.ic.ICgetpinpos("IC2", "p22"))

    def test_LineDraw(self):
        print(self.ic.ICgetpinpos("IC1", "p9")[2])
        print(self.ic.ICgetpinpos("IC2", "p2")[2])
        print(self.ic.gridgraph(self.ic.ICgetpinpos("IC1", "p9")[2], self.ic.ICgetpinpos("IC2", "p2")[2]))
        self.ic.linedraw(self.ic.gridgraph(self.ic.ICgetpinpos("IC1", "p9")[2], self.ic.ICgetpinpos("IC2", "p2")[2])[0])
        self.ic.show()

unittest.main()
