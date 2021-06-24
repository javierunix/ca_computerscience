class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex):
        print("Adding edge to " + vertex)
        self.edges[vertex] =  True


    def get_edges(self):
        return list(self.edges.keys())

