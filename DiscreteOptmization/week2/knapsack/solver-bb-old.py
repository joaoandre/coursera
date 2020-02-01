#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])


class State(object):
    def __init__(self, level, benefit, weight, token, data, max_weight):
        self.level = level
        self.benefit = benefit
        self.weight = weight
        self.token = token
        self.data = data
        self.max_weight = max_weight
        self.available = self.token[:self.level] + [1]*(len(data)-level)
        self.ub = self.upperbound()

    def upperbound(self):
        upperbound = 0

        weight_acumulated = 0

        for avail, (_, wei, val) in zip(self.available, self.data):
            _wei = wei * avail
            if _wei <= self.max_weight - weight_acumulated:
                weight_acumulated = _wei
                upperbound += val * avail
            else:
                upperbound += val * (self.max_weight - weight_acumulated) / _wei
                break
        return upperbound

    def develop(self):
        level = self.level + 1
        _, weight, value = self.data[self.level]
        left_weight = self.weight + weight

        if left_weight <= self.max_weight:
            left_benefit = self.benefit + value
            left_token = self.token[:self.level] + [1] + self.token[level:]
            left_child = State(level, left_benefit, left_weight, left_token, self.data, self.max_weight)
        else:
            left_child = None

        right_child = State(level, self.benefit, self.weight, self.token, self.data, self.max_weight)
        return ([] if left_child is None else [left_child]) + [right_child]


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    data_weight = []
    data_value = []
    data_item = []
    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()

        data_value.append(int(parts[0]))
        data_weight.append(int(parts[1]))
        data_item.append(i-1)

        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    data_sorted = sorted(zip(data_item, data_weight, data_value),
                         key=lambda (i, w, v): v//w, reverse=True)
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    # weight = 0
    # taken = [0] * len(items)
    #
    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight

    root = State(0, 0, 0, [0] * len(data_sorted), data_sorted, capacity)
    waiting_states = []
    current_state = root

    while current_state.level < len(data_sorted):
        waiting_states.extend(current_state.develop())
        waiting_states.sort(key=lambda x: x.ub)

        current_state = waiting_states.pop()
    best_item =[tok for tok, (item, _, _) in zip(current_state.token, data_sorted)]

    # print "Total weight: ", current_state.weight
    # print "Total Value: ", current_state.benefit
    # print "Items:", best_item

    # prepare the solution in the specified output format
    output_data = str(current_state.benefit) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, best_item))
    return output_data



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

