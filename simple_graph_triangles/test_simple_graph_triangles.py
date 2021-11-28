from simple_graph_triangles import SimpleGraph


def test_add_vertex():
    s = SimpleGraph(8)
    s.AddVertex(0)
    s.AddVertex(1)
    s.AddEdge(0, 1)
    assert s.vertex[0].Value == 0
    assert s.vertex[1].Value == 1
    assert s._connection_indices(0) == [1]
    assert s._connection_indices(1) == [0]
    s.AddVertex(2)
    s.AddEdge(0, 2)
    assert s._connection_indices(0) == [1, 2]
    assert s._connection_indices(2) == [0]
    assert s._is_weak(0)
    assert s._is_weak(1)
    assert s._is_weak(2)


def test_is_weak_one_vertex():
    s = SimpleGraph(8)
    s.AddVertex(0)
    s.AddVertex(1)
    s.AddVertex(2)
    s.AddEdge(0, 1)
    s.AddEdge(0, 2)
    s.AddEdge(1, 2)
    assert not s._is_weak(0)
    assert not s._is_weak(1)
    assert not s._is_weak(2)
    s.AddVertex(3)
    s.AddEdge(1, 3)
    assert not s._is_weak(0)
    assert not s._is_weak(1)
    assert not s._is_weak(2)
    assert s._is_weak(3)


def test_weak_vertices():
    s = SimpleGraph(8)
    s.AddVertex(0)
    s.AddVertex(1)
    s.AddVertex(2)
    s.AddEdge(0, 1)
    s.AddEdge(0, 2)
    s.AddEdge(1, 2)
    s.AddVertex(3)
    s.AddEdge(1, 3)
    assert s.WeakVertices() == [s.vertex[3]]


def test_weak_vertices_from_pic():
    s = SimpleGraph(10)
    s.AddVertex(0)
    s.AddVertex(1)
    s.AddVertex(2)
    s.AddVertex(3)
    s.AddVertex(4)
    s.AddVertex(5)
    s.AddVertex(6)
    s.AddVertex(7)
    s.AddVertex(8)
    s.AddEdge(0, 1)
    s.AddEdge(0, 2)
    s.AddEdge(0, 4)

    s.AddEdge(1, 2)
    s.AddEdge(1, 3)

    s.AddEdge(2, 3)
    s.AddEdge(2, 5)

    s.AddEdge(4, 5)

    s.AddEdge(5, 6)
    s.AddEdge(5, 7)

    s.AddEdge(6, 7)
    s.AddEdge(7, 8)
    res = s.WeakVertices()

    assert res == [s.vertex[4], s.vertex[8]]
