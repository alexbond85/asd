class Vertex:

    def __init__(self, val):
        self.Value = val
        self.is_stable = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def _connection_indices(self, vertex_index):
        res = []
        for i, x in enumerate(self.m_adjacency[vertex_index]):
            if x == 1:
                res.append(i)
        return res

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

    def _all_pairs(self, a):
        res = []
        for i, x in enumerate(a):
            for j in a[i + 1:]:
                res.append((x, j))
        return res

    def _is_weak(self, v: int):
        vertex = self.vertex[v]
        adjacent_vertices_indices = self._connection_indices(v)
        if len(adjacent_vertices_indices) < 2:
            vertex.is_stable = False
            return True
        indices_pairs = self._all_pairs(adjacent_vertices_indices)
        for pair in indices_pairs:
            v1, v2 = pair
            v1_values = self.m_adjacency[v1][v], self.m_adjacency[v1][v1], self.m_adjacency[v1][v2]
            v2_values = self.m_adjacency[v2][v], self.m_adjacency[v2][v1], self.m_adjacency[v2][v2]
            v_values = self.m_adjacency[v][v], self.m_adjacency[v][v1], self.m_adjacency[v][v2]
            if sum([v_values[i] + v1_values[i] + v2_values[i] for i in range(3)]) == 6:
                vertex.is_stable = True
                self.vertex[v1].is_stable = True
                self.vertex[v2].is_stable = True
                return False
        return True

    def _reset_all_vertices_to_weak(self):
        for vertex in self.vertex:
            if vertex is not None:
                vertex.is_stable = False

    def WeakVertices(self):
        self._reset_all_vertices_to_weak()
        res = []
        for v_index, v in enumerate(self.vertex):
            if v and not v.is_stable:
                is_weak = self._is_weak(v_index)
                if is_weak:
                    res.append(v)
        return res
