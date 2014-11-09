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
        self.assertEqual(self.analysis.text('ic A:'), {'type': 'ic', 'name': 'A'})
        self.assertEqual(self.analysis.text('left:'), {'type': 'icleft', 'name': ':'})
        self.assertEqual(self.analysis.text('B'), {'type': 'string', 'name': 'B'})
        self.assertEqual(self.analysis.text('A.B-C.D'), {'type': 'wire', 'list': [{'name': 'A', 'pin': 'B'}, {'name': 'C', 'pin': 'D'}]})
        self.assertEqual(self.analysis.text('end'), {'name': 'end', 'type': 'END'})
        data = '''
        ic A:
        left:
            B
            C
        end
        right:
            D
            E
        end
        bottom:
            F
            G
        end
        top:
            H
            I
        end
        end
        main:
            A.B-A.C
        end
        '''
        self.analysis.run(data)


if __name__ == '__main__':
    unittest.main()
