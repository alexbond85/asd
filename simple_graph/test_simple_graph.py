from simple_graph import Vertex, SimpleGraph


def test_add_vertex():
    s = SimpleGraph(2)
    s.AddVertex(2)
    assert s.vertex[0].Value == 2


def test_add_edge():
    s = SimpleGraph(2)
    s.AddVertex(2)
    s.AddVertex(3)
    assert s.vertex[0].Value == 2
    assert s.vertex[1].Value == 3
    s.AddEdge(0, 1)
    assert s.m_adjacency == [[0, 1], [1, 0]]

    s = SimpleGraph(3)
    s.AddVertex(1)
    s.AddVertex(2)
    s.AddVertex(3)
    assert s.vertex[0].Value == 1
    assert s.vertex[1].Value == 2
    assert s.vertex[2].Value == 3
    s.AddEdge(0, 2)
    assert s.m_adjacency == [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
    s.AddEdge(0, 2)
    assert s.m_adjacency == [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
    s.AddEdge(1, 2)
    assert s.m_adjacency == [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
    s.RemoveEdge(1, 2)
    assert s.m_adjacency == [[0, 0, 1], [0, 0, 0], [1, 0, 0]]


def test_is_edge():
    s = SimpleGraph(2)
    s.AddVertex(2)
    s.AddVertex(3)
    assert s.vertex[0].Value == 2
    assert s.vertex[1].Value == 3
    s.AddEdge(0, 1)
    assert s.m_adjacency == [[0, 1], [1, 0]]
    assert s.IsEdge(0, 1)


