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
    for row in range(nrows):
        G.add_edge("start", node_name(row, 0), weight=weights[row][0])
        G.add_edge(node_name(row, 0), node_name(row, 1), weight=weights[row][1])
        G.add_edge(node_name(row, ncols-1), "finish", weight=0)
        for col in range(1, ncols-1):
            G.add_edge(node_name(row, col), node_name(row, col+1), weight=weights[row][col+1])
            if row > 0:
                G.add_edge(node_name(row, col), node_name(row-1, col), weight=weights[row-1][col])
            if row < nrows-1:
                G.add_edge(node_name(row, col), node_name(row+1, col), weight=weights[row+1][col])
    assert(G.out_degree(start) == nrows)
    assert(G.in_degree(finish) == nrows)
    path = networkx.shortest_path(G, start, finish, weight='weight')
    path_weights = [G.edge[path[i]][path[i+1]]['weight'] for i in range(len(path)-2)]
    print "{}".format(sum(path_weights))
