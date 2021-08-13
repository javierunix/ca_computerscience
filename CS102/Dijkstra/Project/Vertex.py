class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight=0):
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())

  # create a new method that takes in an edge and returns the weight of that edge.

  def get_edge_weight(self, edge):
    return self.edges[edge]