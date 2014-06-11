#!/usr/bin/env python

import networkx
import matplotlib.pyplot as plt

def get_weights_from_stdin():
    import fileinput
    from ast import literal_eval
    matrix = []
    for line in fileinput.input():
        matrix.append(list(literal_eval(line)))
    return matrix

def node_name(row, col):
    return "_{}_{}_".format(row, col)

def add_up_edge(G, row, col):
    s = node_name(row, col)
    d = node_name(row-1, col)
    w=weights[row-1][col]
    G.add_edge(s, d, weight=w)

def add_down_edge(G, row, col):
    s = node_name(row, col)
    d = node_name(row+1, col)
    w = weights[row+1][col]
    G.add_edge(s, d, weight=w)

def add_left_edge(G, row, col):
    s = node_name(row, col)
    d = node_name(row, col-1)
    w = weights[row][col-1]
    G.add_edge(s, d, weight=w)

def add_right_edge(G, row, col):
    s = node_name(row, col)
    d = node_name(row, col+1)
    w = weights[row][col+1]
    G.add_edge(s, d, weight=w)

if __name__ == '__main__':
    weights = get_weights_from_stdin()
    start = "start"
    finish = "finish"
    G = networkx.DiGraph()
    G.add_node(start)
    G.add_node(finish)
    nrows = len(weights)
    ncols = len(weights[0])
    for row in range(nrows):
        for col in range(ncols):
            G.add_node(node_name(row, col))
    G.add_edge("start", node_name(0, 0), weight=weights[0][0])
    G.add_edge(node_name(nrows-1, ncols-1), "finish", weight=0)
    for row in range(nrows):
        for col in range(ncols):
            if row > 0:
                add_up_edge(G, row, col)
            if row < nrows-1:
                add_down_edge(G, row, col)
            if col > 0:
                add_left_edge(G, row, col)
            if col < ncols-1:
                add_right_edge(G, row, col)
    path = networkx.shortest_path(G, start, finish, weight='weight')
    path_weights = [G.edge[path[i]][path[i+1]]['weight'] for i in range(len(path)-2)]
    print "{}".format(sum(path_weights))
