#!coding:utf-8

import sys
import analysis
import draw_graphics

if __name__ == '__main__':
    filename = sys.argv[1]
    ic_pos = [(int(sys.argv[2].split(',')[0]), int(sys.argv[2].split(',')[1]))]
    ic_pos.append((int(sys.argv[3].split(',')[0]), int(sys.argv[3].split(',')[1])))
    sourcecode = open(filename, 'r').read()
    analysis = analysis.Analysis()
    ic = draw_graphics.Draw()
    analysis.run(sourcecode)
    for count, i in enumerate(analysis.ic_info):
        top_len = i['top_len']
        bottom_len = i['bottom_len']
        left_len = i['left_len']
        right_len = i['right_len']
        ic.pin(top=top_len, bottom=bottom_len, left=left_len, right=right_len)
        top = list(map(lambda s: s['name'], i['top']))
        bottom = list(map(lambda s: s['name'], i['bottom']))
        left = list(map(lambda s: s['name'], i['left']))
        right = list(map(lambda s: s['name'], i['right']))
        ic.text(top=top, bottom=bottom, left=left, right=right)
        ic.draw(ic_pos[count][0], ic_pos[count][1])
        ic.name(i['ic_name'])

    for i in analysis.main_info:
        name1 = i['list'][0]['name']
        name2 = i['list'][1]['name']
        pin1 = i['list'][0]['pin']
        pin2 = i['list'][1]['pin']
        ic.line_draw(ic.grid_graph(ic.get_pin_pos(name1, pin1)[2], ic.get_pin_pos(name2, pin2)[2])[0])
    ic.show()
