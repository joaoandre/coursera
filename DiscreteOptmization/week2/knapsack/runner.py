from knapsack import Knapsack
class Item:
  def __init__(self, value, cost):
    self.value = value
    self.cost = cost

items = [
 # test 1: capacity 20
  # Item(3, 7),
  # Item(5, 3),
  # Item(4, 8),
  # Item(9, 3),
  # Item(10, 9),
  # Item(6, 11)
 # test 2: capacity 60
  # Item(30, 5),
  # Item(20, 10),
  # Item(100, 20),
  # Item(90, 30),
  # Item(160, 40)
 # test 3: capacity 15
  Item(10, 2),
  Item(10, 4),
  Item(12, 6),
  Item(18, 9)
]
for i in Knapsack(items, capacity=15).pack():
  print(str(i.value) + "-" + str(i.cost))