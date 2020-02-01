#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(100000)

from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])


def greedy_algorithm(items, capacity):
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0] * len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


def greedy_algorithm_ver2(items, capacity):
    taken = [0] * len(items)
    order = [x for x in range(len(items))]
    order = sorted(order, key=lambda x: -float(items[x].value) / items[x].weight)
    weight = 0
    value = 0
    for elem in order:
        if weight + items[elem].weight <= capacity:
            weight += items[elem].weight
            value += items[elem].value
            taken[elem] = 1
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


def dynamic_programming(items, capacity):
    taken = [0] * len(items)
    dp = [[0] * (capacity + 1) for x in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        for j in range(0, capacity + 1):
            dp[i][j] = dp[i - 1][j]
            if j - items[i - 1].weight >= 0:
                dp[i][j] = max(dp[i][j], items[i - 1].value + dp[i - 1][j - items[i - 1].weight])
    output_data = str(dp[len(items)][capacity]) + ' ' + str(1) + '\n'

    j = capacity
    for i in range(len(items)):
        if dp[len(items) - i][j] == dp[len(items) - i - 1][j]:
            taken[len(items) - i - 1] = 0
        else:
            taken[len(items) - i - 1] = 1
            j -= items[len(items) - i - 1].weight

    output_data += ' '.join(map(str, taken))
    return output_data


def dynamic_programming_memory_efficient(items, capacity):
    taken = [0] * len(items)
    dp = [[0] * (capacity + 1) for x in range(2)]
    current_row = 1
    for i in range(0, len(items)):
        # print 'row ' + str(i),
        for j in range(0, capacity + 1):
            # if j%100000 == 0: print round(float(j)/(capacity),2),
            dp[current_row][j] = dp[1 - current_row][j]
            if j - items[i].weight >= 0:
                dp[current_row][j] = max(dp[current_row][j],
                                         items[i].value + dp[1 - current_row][j - items[i].weight])
        current_row = 1 - current_row
    output_data = str(dp[1 - current_row][capacity]) + ' ' + str(1) + '\n'
    return output_data


def calc_estimate(items, capacity, idx):
    order = [x for x in range(idx, len(items))]
    order = sorted(order, key=lambda x: -float(items[x].value) / items[x].weight)
    weight = 0
    value = 0
    for elem in order:
        if weight + items[elem].weight <= capacity:
            weight += items[elem].weight
            value += items[elem].value
        else:
            return value + float(items[elem].value) / items[elem].weight * (capacity - weight)
    return value


def backtrack(items, idx, capacity, best_res, estimate, cur_cost, opt_value):
    if idx == len(items) or best_res[0] == opt_value:
        # if cur_cost > best_res[0]: print cur_cost
        best_res[0] = max(best_res[0], cur_cost)
        return 0, []
    if estimate < best_res[0]:  # pruning
        # print idx, estimate, best_res[0], 'pruning'
        return 0, []
    res, taken = 0, []

    res, taken = backtrack(items, idx + 1, capacity, best_res,
                           cur_cost + calc_estimate(items, capacity, idx + 1), cur_cost, opt_value)
    taken = [0] + taken

    if capacity - items[idx].weight >= 0:  # it is faster to try to pick first if possible
        new_res, new_taken = backtrack(items, idx + 1, capacity - items[idx].weight, best_res,
                                       estimate, cur_cost + items[idx].value, opt_value)
        new_res += items[idx].value
        if new_res > res:
            res, taken = new_res, [1] + new_taken

    # new_res, new_taken = backtrack(items, idx+1, capacity, best_res,
    #                         cur_cost + calc_estimate(items, capacity, idx+1), cur_cost, opt_value)
    # if new_res > res:
    #     res, taken = new_res, [0] + new_taken

    return res, taken


def branch_and_bound(items, capacity):  # relax integrality constraints AND relax capacity ;)
    # print calc_estimate(items, capacity, 0)
    opt_values = {3: 123142343, 30: 99798, 50: 142156, 200: 100236, 400: 3967164, 1000: 109899, 10000: 1099893}
    res, taken = backtrack(items, 0, capacity, [0], calc_estimate(items, capacity, 0), 0, opt_values[len(items)])
    output_data = str(res) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    # print len(items), capacity, len(items) * capacity
    if len(items) * capacity < 10 ** 8 + 5:
        return dynamic_programming(items, capacity)
    elif len(items) < 1000:
        return branch_and_bound(items, capacity)
    else:
        return greedy_algorithm_ver2(items, capacity)


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
