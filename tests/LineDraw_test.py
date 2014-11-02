#!coding:utf-8
import sys
sys.path.append('zamza')

import unittest
import LineDraw

class testLineDraw(unittest.TestCase):
    def setUp(self):
        self.linedraw = LineDraw.LineDraw()

    def testgridnum(self):
        self.assertEqual(self.linedraw.gridnum(10), 1)
        self.assertEqual(self.linedraw.gridnum(100), 10)

if __name__ == '__main__':
    unittest.main()
