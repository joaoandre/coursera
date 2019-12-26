#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []
    weights = []
    values = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        v = int(parts[0])
        w = int(parts[1])
        d = v / w
        weights.append(w)
        values.append(v)
        items.append(Item(i - 1, v, w, d))

    # # Sort the items
    # items = sorted(items, key=lambda x: x.density, reverse=True)
    n = len(items)
    cache = {}
    value, keep = zeroOneKnapsack(values, weights, capacity)
    # print(value)
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, keep))
    return output_data


def greedy_solution(n, k, items):
    value = 0
    weight = 0
    taken = [0] * n

    for item in items:
        if weight + item.weight <= k:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    return value, taken

def total_value(items, max_weight):
    return sum([x.value for x in items]) if sum([x.weight for x in items]) <= max_weight else 0

# v = list of item values or profit
# w = list of item weight or cost
# W = max weight or max cost for the knapsack
def zeroOneKnapsack(v, w, W):
    # c is the cost matrix
    c = []
    n = len(v)
    c = zeros(n, W + 1)
    for i in range(0, n):
        # for ever possible weight
        for j in range(0, W + 1):
            # can we add this item to this?
            if (w[i] > j):
                c[i][j] = c[i - 1][j]
            else:
                c[i][j] = max(c[i - 1][j], v[i] + c[i - 1][j - w[i]])
    return [c[n - 1][W], getUsedItems(w, c)]


# w = list of item weight or cost
# c = the cost matrix created by the dynamic programming solution
def getUsedItems(w, c):
    # item count
    i = len(c) - 1
    currentW = len(c[0]) - 1
    # set everything to not marked
    marked = []
    for i in range(i + 1):
        marked.append(0)
    while (i >= 0 and currentW >= 0):
        if (i == 0 and c[i][currentW] > 0) or c[i][currentW] != c[i - 1][currentW]:
            marked[i] = 1
            currentW = currentW - w[i]
        i = i - 1
    return marked


def zeros(rows, cols):
    row = []
    data = []
    for i in range(cols):
        row.append(0)
    for i in range(rows):
        data.append(row[:])
    return data


def bb_solution(v, w, c):
    sol = 0
    n = len(v)
    idxs = list(range(n))
    idxs.sort(key=lambda i: v[i]/w[i], reverse=True)

    def bound(sw, sv, m):
        if m == n:
            return sv
        objs = ((v[i], w[i]) for i in idxs[m:])

        for av, aw in objs:
            if sw + aw > c:
                break
            sw += aw
            sv += av
        return sv + (av/aw) * (c-sw)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
