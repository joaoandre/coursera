#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
import queue

Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])
# Node = namedtuple("Node", ["level", "profit", "bound", "weight"])

class Node(object):

    def __init__(self, level=-1, profit=0, weight=0, bound=0):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound


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

    # Sort the items
    items = sorted(items, key=lambda x: x.density, reverse=True)
    n = len(items)

    value = bb_solution(items, capacity, n)
    # print(value)
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, []))
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


def bound(u, n, max_weight, items):
    if u.weight >= max_weight:
        return 0
    
    profit_bound = u.profit

    j = u.level + 1
    total_weight = u.weight

    while j < n and total_weight + items[j].weight <= max_weight:
        total_weight += items[j].weight
        profit_bound += items[j].value
        j += 1
    
    if j < n:
        profit_bound += (max_weight - total_weight) * items[j].density
    
    return profit_bound

def bb_solution(items, max_weight, n):
    q = queue.Queue()
    v = Node()
    _u = Node()
    
    q.put(_u)

    max_profit = 0

    while not q.empty():
        u = q.get()

        if u.level == -1:
            v.level = 0
        if u.level == n-1:
            continue

        v.level = u.level + 1

        v.weight = u.weight + items[v.level].weight
        v.profit = u.profit + items[v.level].value

        if v.weight <= max_weight and v.profit > max_profit:
            max_profit = v.profit
        
        v.bound = bound(v, n, max_weight, items)

        if v.bound > max_profit:
            q.put(v)
    
    return max_profit

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
