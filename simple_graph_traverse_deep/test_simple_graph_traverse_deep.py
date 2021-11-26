from simple_graph_traverse_deep import SimpleGraph


def test_depth_first_search():
    s = SimpleGraph(2)
    s.AddVertex(2)
    s.AddVertex(3)
    s.AddEdge(0, 1)
    assert s.DepthFirstSearch(0, 1) == [s.vertex[0], s.vertex[1]]


def test_depth_first_search_three_elem():
    s = SimpleGraph(5)
    s.AddVertex(1)
    s.AddVertex(2)
    s.AddVertex(3)
    s.AddEdge(0, 1)
    s.AddEdge(1, 2)
    assert s.DepthFirstSearch(0, 2) == [s.vertex[0], s.vertex[1], s.vertex[2]]


def test_depth_first_search_five_elem():
    s = SimpleGraph(8)
    s.AddVertex(1)
    s.AddVertex(2)
    s.AddVertex(3)
    s.AddVertex(4)
    s.AddVertex(5)
    s.AddVertex(6)
    s.AddEdge(0, 1)
    s.AddEdge(0, 3)
    s.AddEdge(1, 3)
    s.AddEdge(3, 2)
    s.AddEdge(1, 4)
    s.AddEdge(2, 4)
    s.AddEdge(3, 5)
    r = s.DepthFirstSearch(0, 2)
    assert s.DepthFirstSearch(0, 2) == [s.vertex[0], s.vertex[1], s.vertex[3], s.vertex[2]]
