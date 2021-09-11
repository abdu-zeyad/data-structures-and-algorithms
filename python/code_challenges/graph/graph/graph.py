from python.code_challenges.linked_list.linked_list.linked_list import Node


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        self.adjacency_list[node] = []

    def add_edge(self, start_node, end_node, weight=1):
        if start_node not in self.adjacency_list:
            self.adjacency_list[start_node] = [{end_node: weight}]
        else:
            self.adjacency_list[start_node].append({end_node: weight})

    def get_nodes(self):
        return self.adjacency_list.keys()

    def get_neighbors(self, node):
        output = []
        for x in self.adjacency_list[node]:
            output.append(x)
        return output

    def size(self):
        return len(self.adjacency_list)
