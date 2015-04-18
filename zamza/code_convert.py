# coding:utf-8
import shlex


class CodeConvert(object):
    def __init__(self, text):
        self.text = text
        self.shlex_data = shlex.shlex(text)
        self.shlex_data.quotes = '.'

    def connect_line(self):
        res = []
        val = []
        for token in self.shlex_data:
            if token in ';':
                res.append(val)
                val = []
            elif token not in '-':
                val.append(token)
        if val != []:
            res.append(val)
        return res
