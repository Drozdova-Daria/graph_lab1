import collections
import networkx as nx

from draw import Draw


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
        self.graph_dict = dict
        if filename != '':
            self.graph_dict = read_graph_in_dict(filename)
            self.graph = create_graph(self.graph_dict)
        elif dict is not None:
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

    def dfs(self, root, visited=None):
        if visited is None:
            visited = []
        if root not in visited:
            visited.append(root)
            for next in self.graph_dict[root]:
                visited = self.dfs(next, visited)
        return visited

    def draw_graph_path_in_gif(self, vertexes, path):
        draw_mode = Draw(self.graph)
        draw_mode.draw_path_gif(path, vertexes)
