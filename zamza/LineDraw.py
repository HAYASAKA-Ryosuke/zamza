#!coding:utf-8
from PIL import ImageDraw, Image, ImageFont
import networkx
from itertools import repeat


class Linedraw(object):
    def __init__(self):
        self.space = 10
        self.startx = None
        self.starty = None
        self.stopx = None
        self.stopy = None
        self.nx = networkx
        self.graph = self.nx.DiGraph()

    def linedraw(self, linelist, linecolor='black'):
        self.drawline.line(linelist, fill=linecolor)

    def _add_edge(self, gridlist, i, j, com):
        if com == 'y_up':
            self.graph.add_edge(gridlist[i][j], gridlist[i][j - 1], weight=1)
        if com == 'y_down':
            self.graph.add_edge(gridlist[i][j], gridlist[i][j + 1], weight=1)
        if com == 'x_up':
            self.graph.add_edge(gridlist[i][j], gridlist[i + 1][j], weight=1)
        if com == 'x_down':
            self.graph.add_edge(gridlist[i][j], gridlist[i - 1][j], weight=1)

    def _grid_if(self, gridlist, i, j, xlast, ylast):
        self.graph.add_node(gridlist[i][j])
        if i == 0:
            if j < xlast:
                self._add_edge(gridlist, i, j, 'y_down')
            self._add_edge(gridlist, i, j, 'x_up')
        elif i == ylast:
            if j < xlast:
                self._add_edge(gridlist, i, j, 'y_down')
        else:
            if i < ylast:
                self._add_edge(gridlist, i, j, 'x_up')
            self._add_edge(gridlist, i, j, 'x_down')
            if j < xlast:
                self._add_edge(gridlist, i, j, 'y_down')
            self._add_edge(gridlist, i, j, 'y_up')

    def gridgraph(self, start=[], stop=[]):
        gridlist = self.gridnumlist(start, stop)
        xlast = len(gridlist[0]) - 1
        ylast = len(gridlist) - 1
        # for i in range(ylast + 1):
        #     for j in range(xlast + 1):
        [self._grid_if(gridlist, i, j, xlast, ylast) for j in range(xlast + 1) for i in range(ylast + 1)]
        return [p for p in self.nx.all_shortest_paths(self.graph, tuple(start), tuple(stop))]

    def _gridnum(self, xsmall, ysmall, xlarge, ylarge):
        pos = lambda x, y: (xsmall + (self.space * x), ysmall + (self.space * y),)
        interval_space = lambda pixel: round(pixel / self.space) + 1
        yseparate = interval_space(ylarge - ysmall)
        xseparate = interval_space(xlarge - xsmall)
        return [[pos(j, i) for j in range(xseparate)] for i in range(yseparate)]

    def gridnumlist(self, start=[], stop=[]):
        if start[0] <= stop[0] and start[1] < stop[1]:
            return self._gridnum(start[0], start[1], stop[0], stop[1])
        elif start[0] >= stop[0] and start[1] < stop[1]:
            return self._gridnum(stop[0], start[1], start[0], stop[1])
        elif start[0] <= stop[0] and start[1] > stop[1]:
            return self._gridnum(start[0], stop[1], stop[0], start[1])
        elif start[0] >= stop[0] and start[1] > stop[1]:
            return self._gridnum(stop[0], stop[1], start[0], start[1])
