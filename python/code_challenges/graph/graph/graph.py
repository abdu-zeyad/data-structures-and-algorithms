from python.code_challenges.stack_and_graph.stack_and_graph.stack_and_queue import Queue


class Node:
    def __init__(self, value):
        self.value = value


class Graph:
    def __init__(self):
        self.adjList = {}

    def add_node(self, value):
        node = Node(value)
        self.adjList[node.value] = []

    def add_edge(self, start, end):
        if start.value not in self.adjList:
            self.adjList[start.value] = [{end.value}]
            print(start.value)
        else:
            self.adjList[start.value].append({end.value})

    def size(self):
        return len(self.adjList)

    def get_nodes(self):
        return list(self.adjList.keys())

    def get_neighbors(self, node):
        output = []
        for x in self.adjList[node]:
            output.append(x)
        return output

    def bfs(self, start_node):
        nodes = []
        visited = set()
        breadth = Queue()
        breadth.enqueue(start_node)

        visited.add(start_node)
        while breadth.length() > 0:
            node = breadth.dequeue()
            print(node)
            nodes.append(node)
            print(self.adjList[node])
            for n in self.adjList[node]:
                if n not in visited:
                    breadth.enqueue(n)
                    visited.add(n)

        return nodes


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
graph.bfs(1)
