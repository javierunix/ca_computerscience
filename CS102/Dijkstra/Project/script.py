import random
from random import randrange
from Graph import Graph
from Vertex import Vertex

def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)

def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g

# Define your functions below:

# this function checks if all vertices as been visited
def visited_all_vertices(visited_status):
  for vertex in visited_status:
    if visited_status[vertex] == 'unvisited':
      return False
  return True 

def traveling_salesperson(graph):
  final_path = "" # initialize final path as empty string

  # create a dictionary that holds vertices and their statuses
  visited_status = {vertex: 'unvisited' for vertex in graph.graph_dict} # all vertices start as unvisited

  # select an initial vertex at random. Label it as the current_vertex, then mark it as visited and add it to the final path.
  current_vertex = random.choice(list(graph.graph_dict))
  visited_status[current_vertex] = "visited"
  final_path += current_vertex

  # check if all vertices has been visited
  visited_all = visited_all_vertices(visited_status)    