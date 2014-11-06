#!coding:utf-8
import unittest
import sys
sys.path.append('zamza')
import Analysis


class Analysistest(unittest.TestCase):
    def setUp(self):
        self.analysis = Analysis.Analysis()

    def testtext(self):
        self.assertEqual(self.analysis.text('import A'), {'type': 'import', 'name': 'A'})
        self.assertEqual(self.analysis.text('parts A:'), {'type': 'parts', 'name': 'A'})
        self.assertEqual(self.analysis.text('A.B-C.D'), [{'name': 'A', 'pin': 'B'}, {'name': 'C', 'pin': 'D'}])

if __name__ == '__main__':
    unittest.main()
