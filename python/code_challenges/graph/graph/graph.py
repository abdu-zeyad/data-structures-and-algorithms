class Node:
    def __init__(self, value):
        self.value = value


class Graph:
    def __init__(self):
        self.adjList = {}

    def add_node(self, value):
        node = Node(value)
        self.adjList[node.value] = []
        print(self.adjList)

    def add_edge(self, start, end):
        if start not in self.adjList:
            self.adjList[start] = [{end}]
        else:
            self.adjList[start].append({end})

    def size(self):
        return len(self.adjList)

    def get_nodes(self):
        return list(self.adjList.keys())

    def get_neighbors(self, node):
        output = []
        for x in self.adjList[node]:
            output.append(x)
        return output


graph = Graph()
graph.add_node(5)
graph.add_node(4)
graph.add_node(3)
graph.add_node(2)
graph.add_node(1)
graph.add_edge(1, 3)
graph.add_edge(4, 2)
graph.add_edge(5, 3)
graph.add_edge(1, 5)
graph.add_edge(2, 4)

print(graph.get_neighbors(4))
