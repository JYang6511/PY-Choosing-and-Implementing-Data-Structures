class Node:
  def __init__(self, data, reference=None):
    self.data = data
    self.reference = reference

  node1 = Node(5)
  print(node1.data)
