class Node:
    CAP = 0

    def __init__(self, _index, item, upperbound, parent):
        self.index = _index
        self.item = item
        self.upperbound = upperbound
        self.parent = parent
        self.negative_child = None
        self.positive_child = None

    def cap_negative_child(self):
        self.negative_child = Node.CAP

    def cap_positive_child(self):
        self.negative_child = Node.CAP

    def cost(self):
        if self.parent:
            return self.parent.cost() + self.item.cost if self.item else 0
        return 0

    def items(self):
        if self.parent:
            if self.item:
                _items = self.parent.items()
                _items.append(self.item)
                return _items
            return self.parent.items()
        return []

    def leaf(self):
        return self.negative_child == Node.CAP and self.positive_child == Node.CAP

    def negative_child_growable(self):
        return self.negative_child is None

    def positive_child_growable(self):
        return self.positive_child is None

    def value(self):
        if self.parent:
            return self.parent.value() + (self.item.value if self.item else 0)
        return 0
