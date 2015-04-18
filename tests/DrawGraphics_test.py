# coding:utf-8

import sys
sys.path.append('zamza')

import draw_graphics
import unittest


class testDrawGraphics(unittest.TestCase):
    def setUp(self):
        x = 50
        y = 50
        self.ic = draw_graphics.Draw()
        self.ic.pin(top=0, left=8, bottom=0, right=8)
        self.ic.text(top=[],
                left=["pa1", "pa2", "pa3", "pa4", "pa5", "pa6", "pa7", "pa8"],
                bottom=[],
                right=["pa9", "pa10", "pa11", "pa12", "pa13", "pa14", "pa15", "pa16"]
                )
        self.ic.draw(x, y)
        self.ic.name("IC1")

        x = 300
        y = 300
        self.ic.pin(top=8, left=8, bottom=8, right=8)
        self.ic.text(top=["pb1", "pb2", "pb3", "pb4", "pb5", "pb6", "pb7", "pb8"],
                left=["pb9", "pb10", "pb12", "pb13", "pb14", "pb15", "pb16", "pb17"],
                bottom=["pb18", "pb19", "pb20", "pb21", "pb22", "pb23", "pb24", "pb25"],
                right=["pb26", "pb27", "pb28", "pb29", "pb30", "pb31", "pb32", "pb33"]
                )
        self.ic.draw(x, y)
        self.ic.name("IC2")

    def test_getpinpos(self):
        self.assertEqual(("top", 1, (360, 300)), self.ic.get_pin_pos("IC2", "pb2"))
        self.assertEqual(("left", 2, (290, 360)), self.ic.get_pin_pos("IC2", "pb12"))
        self.assertEqual(("right", 7, (550, 470)), self.ic.get_pin_pos("IC2", "pb33"))
        self.assertEqual(("bottom", 4, (420, 510)), self.ic.get_pin_pos("IC2", "pb22"))

    def test_LineDraw(self):
        self.ic.line_draw(self.ic.grid_graph(self.ic.get_pin_pos("IC1", "pa9")[2], self.ic.get_pin_pos("IC2", "pb2")[2])[0])
        self.ic.line_draw(self.ic.grid_graph(self.ic.get_pin_pos("IC1", "pa12")[2], self.ic.get_pin_pos("IC2", "pb18")[2])[0])
        self.ic.line_draw(self.ic.grid_graph(self.ic.get_pin_pos("IC1", "pa15")[2], self.ic.get_pin_pos("IC2", "pb3")[2])[0])
        self.ic.line_draw(self.ic.grid_graph(self.ic.get_pin_pos("IC1", "pa1")[2], self.ic.get_pin_pos("IC2", "pb33")[2])[0])
        self.ic.line_draw(self.ic.grid_graph(self.ic.get_pin_pos("IC1", "pa8")[2], self.ic.get_pin_pos("IC2", "pb9")[2])[0])
        self.ic.show()

unittest.main()
