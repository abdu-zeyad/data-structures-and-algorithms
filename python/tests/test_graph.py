from python.code_challenges.graph.graph.graph import Graph, Vertex


def test_size():
    graph = Graph()
    graph.add_node(5)
    graph.add_node(4)
    graph.add_node(3)
    graph.add_node(2)
    graph.add_node(1)
    actual = graph.size()
    excepted = 5
    assert actual == excepted


def test_get_nodes():
    graph = Graph()
    graph.add_node(5)
    graph.add_node(4)
    graph.add_node(3)
    graph.add_node(2)
    graph.add_node(1)
    actual = graph.get_nodes()
    excepted = [5, 4, 3, 2, 1]
    assert actual == excepted


def test_get_neighbors():
    graph = Graph()
    graph.add_node(5)
    graph.add_node(4)
    graph.add_node(3)
    graph.add_node(2)
    graph.add_node(1)
    graph.add_edge(Vertex(1), Vertex(4))
    graph.add_edge(Vertex(4), Vertex(1))
    graph.add_edge(Vertex(4), Vertex(2))
    graph.add_edge(Vertex(2), Vertex(4))
    graph.add_edge(Vertex(3), Vertex(2))
    actual = graph.get_neighbors(Vertex(4))
    excepted = [1, 2]
    assert actual == excepted
