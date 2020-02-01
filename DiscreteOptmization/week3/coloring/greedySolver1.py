#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import choice


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.adj = {v: [] for v in range(0, vertices)}

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def get_degree(self, n):
        return len(self.adj[n])

    def get_group_by_degree(self, group):
        return sorted(group, key=self.get_degree, reverse=True)

    def greedy_coloring(self, order=None):
        result = [-1] * self.v
        start_index = order[0] if order else 0
        available = [False] * self.v

        if not order:
            order = list(range(0, self.v))
        result[start_index] = 0

        for u in order[1:]:
            for i in self.adj[u]:
                if result[i] != -1:
                    available[result[i]] = True

            for c in range(0, self.v):
                if not available[c]:
                    # c += 1
                    break
            result[u] = c

            available = [False] * self.v
        return result

    def group_solution_by_color(self, solution):
        color_map = {}
        max_color = max(solution) + 1
        for i, c in enumerate(solution):
            if c not in color_map:
                color_map[c] = [i]
                continue
            color_map[c].append(i)
        return color_map, max_color


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])
    g = Graph(node_count)
    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        u, w = int(parts[0]), int(parts[1])
        edges.append((u, w))
        g.add_edge(u, w)
    # build a trivial solution
    # every node has its own color
    order = []
    for i in range(0, 3000):
        solution = g.greedy_coloring(order)

        order = []
        color_map, highest_color = g.group_solution_by_color(solution)
        colors = list(range(highest_color))

        while len(colors) > 0:
            c = colors.pop(choice(range(len(colors))))
            order += g.get_group_by_degree(color_map[c])

    # prepare the solution in the specified output format
    output_data = str(max(solution) + 1) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

