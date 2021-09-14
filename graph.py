adjacentLIst = dict()


airports = ["a", "b", "c", "d"]

routes = [["a", "b"], ["b", "d"], ["a", "c"], ["c", "d"], ["b", "a"], ["c", "a"]]


def add_node(airports):
    adjacentLIst[airports] = []


def add_edge(origin, destination):
    adjacentLIst.get(origin).append(destination)


for i in airports:
    add_node(i)

for i in routes:
    add_edge(i[0], i[1])


print(adjacentLIst)
