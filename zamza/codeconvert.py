# coding:utf-8
import shlex


class CodeConvert(object):
    def __init__(self, text):
        self.text = text
        self.shlexdata = shlex.shlex(text)
        self.shlexdata.quotes = '.'

    def connectline(self):
        res = []
        val = []
        for token in self.shlexdata:
            if token in ';':
                res.append(val)
                val = []
            elif token not in '-':
                val.append(token)
        if val != []:
            res.append(val)
        return res
