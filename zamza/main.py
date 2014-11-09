#!coding:utf-8

import sys
import Analysis
import DrawGraphics

if __name__ == '__main__':
    filename = sys.argv[1]
    sourcecode = open(filename, 'r').read()
    analysis = Analysis.Analysis()
    ic = DrawGraphics.draw()
    analysis.run(sourcecode)
    for i in analysis.icinfo:
        toplen = i['toplen']
        bottomlen = i['bottomlen']
        leftlen = i['leftlen']
        rightlen = i['rightlen']
        ic.ICpin(top=toplen, bottom=bottomlen, left=leftlen, right=rightlen)
        top = list(map(lambda s: s['name'], i['top']))
        bottom = list(map(lambda s: s['name'], i['bottom']))
        left = list(map(lambda s: s['name'], i['left']))
        right = list(map(lambda s: s['name'], i['right']))
        ic.ICtext(top=top, bottom=bottom, left=left, right=right)
        ic.ICdraw(300, 300)
        ic.ICname(i['icname'])

    for i in analysis.maininfo:
        name1 = i['list'][0]['name']
        name2 = i['list'][1]['name']
        pin1 = i['list'][0]['pin']
        pin2 = i['list'][1]['pin']
        ic.linedraw(ic.gridgraph(ic.ICgetpinpos(name1, pin1)[2], ic.ICgetpinpos(name2, pin2)[2])[0])
    ic.show()
