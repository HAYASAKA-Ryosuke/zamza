#!coding:utf-8
import sys
sys.path.append('zamza')

import unittest
import LineDraw

class testLineDraw(unittest.TestCase):
    def setUp(self):
        self.linedraw = LineDraw.LineDraw()

    def testgridnum(self):
        self.assertEqual(self.linedraw.gridnumlist([10,20],[30,30]),[[(10, 20), (20, 20), (30, 20)], [(10, 30), (20, 30), (30, 30)]])
        self.assertEqual(self.linedraw.gridnumlist([10,10],[20,30]),[[(10, 10), (20, 10)], [(10, 20), (20, 20)], [(10, 30), (20, 30)]])
        self.assertEqual(self.linedraw.gridnumlist([30,10],[10,20]),[[(10,10),(20,10),(30,10)],[(10,20),(20,20),(30,20)]])
        self.assertEqual(self.linedraw.gridnumlist([10,30],[30,20]),[[(10,20),(20,20),(30,20)],[(10,30),(20,30),(30,30)]])

    def testgridgraph(self):
        print(self.linedraw.gridgraph([10,20],[30,30]))



if __name__ == '__main__':
    unittest.main()
