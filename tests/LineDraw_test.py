#!coding:utf-8
import sys
sys.path.append('zamza')

import unittest
import LineDraw

class testLineDraw(unittest.TestCase):
    def setUp(self):
        self.linedraw = LineDraw.LineDraw()

    def testgridnum(self):
        self.assertEqual(self.linedraw.gridnumlist(10,20),[])
        self.assertEqual(self.linedraw.gridnumlist(10,30),[20])
        self.assertEqual(self.linedraw.gridnumlist(10,100),[20,30,40,50,60,70,80,90])



if __name__ == '__main__':
    unittest.main()
