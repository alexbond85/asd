from simple_graph_traverse_broad import SimpleGraph


def test_breath_first_search():
    s = SimpleGraph(12)
    s.AddVertex(0)
    s.AddVertex(1)
    s.AddVertex(2)
    s.AddVertex(3)
    s.AddVertex(4)
    s.AddVertex(5)
    s.AddVertex(6)
    s.AddVertex(7)
    s.AddVertex(8)
    s.AddVertex(9)
    s.AddVertex(10)

    s.AddEdge(0, 1)
    s.AddEdge(0, 2)
    s.AddEdge(0, 3)

    s.AddEdge(1, 4)
    s.AddEdge(1, 5)
    s.AddEdge(1, 2)

    s.AddEdge(2, 5)
    s.AddEdge(2, 6)
    s.AddEdge(2, 3)

    s.AddEdge(3, 2)
    s.AddEdge(3, 7)

    s.AddEdge(5, 6)

    s.AddEdge(6, 10)
    s.AddEdge(6, 8)
    s.AddEdge(6, 7)

    s.AddEdge(7, 9)
    s.AddEdge(9, 8)


    print()

    a = s.BreadthFirstSearch(0, 8)
    for i in s._history:
        print(i)
    print(a)
