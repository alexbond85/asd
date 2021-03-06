class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v) -> None:
        v = Vertex(val=v)
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = v
                return

    def RemoveVertex(self, v: int):
        self.vertex[v] = None
        self.m_adjacency[v] = [0] * self.max_vertex
        for i in range(self.max_vertex):
            self.m_adjacency[i][v] = 0

    def IsEdge(self, v1, v2):
        return self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom: int, VTo: int):
        vertex_from = self.vertex[VFrom]
        vertex_to = self.vertex[VTo]
        if VFrom == VTo:
            return [vertex_from, vertex_to]
        for v in self.vertex:
            if v:
                v.Hit = False
        stack = [vertex_from]
        while len(stack) > 0:
            v = stack[len(stack) - 1]
            v.Hit = True
            index_v = self.vertex.index(v)
            indices_adj_vertices = [i for i, val in enumerate(self.m_adjacency[index_v]) if val == 1]
            adj_vertices = [self.vertex[i] for i in indices_adj_vertices]
            adj_vertices = [v for v in adj_vertices if not v.Hit]
            if vertex_to in adj_vertices:
                vertex_to.Hit = True
                stack.append(vertex_to)
                return stack
            if adj_vertices:
                stack.append(adj_vertices[0])
            else:
                stack.pop()
        return stack

