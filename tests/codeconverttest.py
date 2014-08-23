# coding:utf-8
import sys
import unittest
sys.path.append('zamza')
import codeconvert


class testcodeconvert(unittest.TestCase):
    def testconnectline(self):
        cc = codeconvert.CodeConvert(text='IC1.P1-IC2.P2; IC1.P3-IC2.P4')
        self.assertEqual([['IC1.P1', 'IC2.P2'], ['IC1.P3', 'IC2.P4']], cc.connectline())
        cc = codeconvert.CodeConvert(text='IC1.P1-IC2.P2 - IC2.P10; IC1.P3-IC2.P4')
        self.assertEqual([['IC1.P1', 'IC2.P2', 'IC2.P10'], ['IC1.P3', 'IC2.P4']], cc.connectline())
unittest.main()
