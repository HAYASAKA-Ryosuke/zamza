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

    def gridgraph(self, start=[], stop=[]):
        gridlist = self.gridnumlist(start, stop)
        first = 0
        xlast = len(gridlist[0]) - 1
        ylast = len(gridlist) - 1
        for i in range(0, len(gridlist)):
            for j in range(0, len(gridlist[0])):
                self.graph.add_node(gridlist[i][j])
                if i == first:
                    if j < xlast:
                        self.graph.add_edge(gridlist[i][j], gridlist[i][j + 1], weight=1)
                    self.graph.add_edge(gridlist[i][j], gridlist[i + 1][j], weight=1)
                elif i == ylast:
                    if j < xlast:
                        self.graph.add_edge(gridlist[i][j], gridlist[i][j+1],weight=1)
                else:
                    if i < ylast:
                        self.graph.add_edge(gridlist[i][j], gridlist[i+1][j],weight=1)
                    self.graph.add_edge(gridlist[i][j], gridlist[i-1][j],weight=1)
                    if j < xlast:
                        self.graph.add_edge(gridlist[i][j], gridlist[i][j+1],weight=1)
                    self.graph.add_edge(gridlist[i][j], gridlist[i][j-1],weight=1)
        return [p for p in self.nx.all_shortest_paths(self.graph,tuple(start),tuple(stop))]

    def _gridnum(self, xsmall, ysmall, xlarge, ylarge):

        def create_pos(x, y):
            return (xsmall + (self.space * x), ysmall + (self.space * y),)

        def gridseparatenum(pixel):
            """gridをどの間隔で空けるか"""
            return round(pixel / self.space) + 1
        yseparate = gridseparatenum(ylarge - ysmall)
        xseparate = gridseparatenum(xlarge - xsmall)
        return [[create_pos(j, i) for j in range(xseparate)] for i in range(yseparate)]

    def gridnumlist(self, start=[], stop=[]):
        if start[0] <= stop[0] and start[1] < stop[1]:
            return self._gridnum(start[0], start[1], stop[0], stop[1])
        elif start[0] >= stop[0] and start[1] < stop[1]:
            return self._gridnum(stop[0], start[1], start[0], stop[1])
        elif start[0] <= stop[0] and start[1] > stop[1]:
            return self._gridnum(start[0], stop[1], stop[0], start[1])
        elif start[0] >= stop[0] and start[1] > stop[1]:
            return self._gridnum(stop[0], stop[1], start[0], start[1])
