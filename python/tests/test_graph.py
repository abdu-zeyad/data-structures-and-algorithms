from python.code_challenges.graph.graph.graph import Graph, Node


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
    graph.add_edge(Node(1), Node(4))
    graph.add_edge(Node(4), Node(1))
    graph.add_edge(Node(4), Node(2))
    graph.add_edge(Node(2), Node(4))
    graph.add_edge(Node(3), Node(2))
    actual = graph.get_neighbors(4)
    excepted = [{1}, {2}]
    assert actual == excepted
