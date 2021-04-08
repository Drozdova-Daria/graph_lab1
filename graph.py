import collections
import networkx as nx


def read_graph_in_dict(filename):
    with open(filename) as file:
        graph = collections.defaultdict(list)
        for node in file.readlines():
            node = node.rstrip('\n').split(", ")
            graph[node[0]].append(node[1])
    return graph


def create_graph(dict_graph):
    G = nx.Graph()
    for root in dict_graph:
        for vertex in dict_graph[root]:
            G.add_edge(root, vertex)
    return G


class Graph:

    def __init__(self, filename='', dict=None):
        self.graph = nx.Graph()
        self.graph_dict = None
        if filename != '':
            self.graph_dict = read_graph_in_dict(filename)
            self.graph = create_graph(self.graph_dict)
        elif dict is not None:
            self.graph_dict = dict
            self.graph = create_graph(self.graph_dict)

    def bfs(self, root):
        visited, queue = [], collections.deque([root])
        visited.append(root)
        while queue:
            vertex = queue.popleft()
            for neighbour in self.graph_dict[vertex]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited


