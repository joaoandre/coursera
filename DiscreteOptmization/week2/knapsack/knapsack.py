from functools import reduce
from sortedcontainers import SortedSet
from .node import Node


class Knapsack:
    def __init__(self, items, capacity):
        self.items = sorted(items, key=lambda item: float(item.value) / item.cost, reverse=True)
        self.capacity = capacity
        self.candidates = SortedSet(key=lambda node: -(node.upper_bound * 2 ** 16 + node.item_index))

    def pack(self):
        self.make_initial_node()

        while True:
            node = self.select_node_to_grow()
            if node:
                self.grow(node, node.item_index + 1)
            else:
                return self.node_with_highest_value().items()

    def grow(self, node, next_index):
        next_item = self.items[next_index] if next_index < len(self.items) else None

        if node.positive_child_growable():
            if next_item and node.cost() + next_item.cost <= self.capacity:
                upper_bound = node.value() + next_item.value + self.upper_bound_beyond(next_index,
                                                                                       capacity=self.capacity - node.cost() - next_item.cost)
                node.positive_child = Node(next_index, next_item, upper_bound, node)
                self.candidates.add(node.positive_child)
            else:
                node.cap_positive_child()
        elif node.negative_child_growable():
            if next_item:
                upper_bound = node.value() + self.upper_bound_beyond(next_index, capacity=self.capacity - node.cost())
                node.negative_child = Node(next_index, None, upper_bound, node)
                self.candidates.add(node.negative_child)
                self.candidates.remove(node)
            else:
                node.cap_negative_child()

    def upper_bound_beyond(self, prev_index, capacity=0):
        index = prev_index + 1

        if index >= len(self.items):
            return 0
        item = self.items[index]

        if item.cost > capacity:
            return float(item.value) * capacity / item.cost
        else:
            return item.value + self.upper_bound_beyond(index, capacity=capacity - item.cost)

    def make_initial_node(self):
        self.candidates.add(Node(-1, None, self.upper_bound_beyond(-1, capacity=self.capacity), None))

    def select_node_to_grow(self):
        hopeful_node = self.candidates[0]

        if not hopeful_node.leaf():
            return hopeful_node

    def node_with_highest_value(self):
        return reduce(
            lambda provisional, candidate: provisional if provisional.value() >= candidate.value() else candidate,
            self.candidates)
