from python.code_challenges.stack_and_graph.stack_and_graph.stack_and_queue import Queue


class Vertex:
    def __init__(self, value):
        self.value = value


class Graph:
    def __init__(self):
        self.adjacent_list = dict()

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacent_list[vertex.value] = []
        return vertex

    def add_edge(self, start, end):
        if start.value not in self.adjacent_list:
            self.adjacent_list[start.value] = [end.value]

        else:
            self.adjacent_list[start.value].append(end.value)

    def get_nodes(self):
        return list(self.adjacent_list.keys())

    def get_neighbors(self, vertex):
        output = []
        for x in self.adjacent_list[vertex.value]:
            output.append(x)
        return output

    def size(self):
        return len(self.adjacent_list)

    def bfs(self, start):
        nodes = []
        visited = set()
        queue = Queue()
        queue.enqueue(start)
        visited.add(start)
        while queue.size > 0:
            vertex = queue.dequeue()
            nodes.append(vertex)
            neighbors = self.adjacent_list[vertex]

            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
        return nodes


if __name__ == "__main__":

    graph = Graph()
    graph.add_node(5)
    graph.add_node(4)
    graph.add_node(3)
    graph.add_node(2)
    graph.add_node(1)

    graph.add_edge(Vertex(1), Vertex(4))
    graph.add_edge(Vertex(3), Vertex(5))
    graph.add_edge(Vertex(5), Vertex(2))
    graph.add_edge(Vertex(2), Vertex(3))
    graph.add_edge(Vertex(1), Vertex(2))

new branch
#  start with the beggining node which is the origin
# then it is connected to the neighbores if the neighbores is the destinaion it is solver
#  if it is not then visit neighbores's neighbores in a while loop
#  the front of the queue is the origin
