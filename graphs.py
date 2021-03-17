# Adjacency Matrix

# graph = [
# #     A  B  C  D  E
#   A  [0, 1, 0, 0, 0 ]
#   B  [0, 0, 1, 1, 1 ]
#   C  [0, 0, 0, 0, 0 ]
#   D  [0, 0, 0, 0, 0 ]
#   E  [0, 0, 0, 0, 0 ]

#     ]

# # A -> E
# # Starting at A, is B a neighbor?
# print(graph[0][1] == 1)
# print(graph[0])

# # print all neighbors for A: O[V] time
# for index, vertex in enumerate(graph[0]):
#     if vertex == 1:
#         print(index)

# # Add a new connection from C to E
# graph[2][4] = 1


# # Adjacency List

# graph = {
#     "A": set(["B"]),
#     "B": set(["C", "E", "D"]),
#     "C": set("E"),
#     "E": set("D"),
#     "D": set(),
#     }

#     # Are A and B neighbors? O(1)
#     print("B" in graph["A"])

#     # Print all neighbors for B
#     for 


class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}
    def __str__(self):
        return str(self.value) + ' connections: ' + str([x.value for x in self.connections])
    def add_connection(self, vert, weight = 0):
        self.connections[vert] = weight
class Graph:
    def __init__(self):
        self.vertices = {}
        self.count = 0
    def add_vertex(self, value):
        self.count += 1
        new_vert = Vertex(value)
        self.vertices[value] = new_vert
        return new_vert
    def add_edge(self, v1, v2, weight = 0):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].add_connection(self.vertices[v2], weight)
    def get_vertices(self):
        return self.vertices.keys()

graph = Graph()

graph_add_vertex("A")
graph_add_vertex("B ")

graph_add_edge("A", "B")