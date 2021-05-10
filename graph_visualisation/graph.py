# Class for storing the graph structure

import collections
import networkx as nx

from graph_visualisation.draw import Draw


def read_graph_in_dict(filename):
    """ Function for reading file in dict"""
    with open(filename) as file:
        graph = collections.defaultdict(list)
        for node in file.readlines():
            node = node.rstrip('\n').split(": ")
            if len(node) != 2:
                print('Incorrect file grammar')
                return None
            graph[node[0]] = node[1].split(',')
    return graph


def create_graph(dict_graph):
    """ Function for creating graph from dict"""
    if dict_graph is None:
        return None
    else:
        G = nx.Graph()
        for root in dict_graph:
            for vertex in dict_graph[root]:
                G.add_edge(root, vertex)
        return G


class Graph:
    """ Class for work with graph"""

    def __init__(self, filename='', dict=None):
        self.graph_dict = dict
        if filename != '':
            self.graph_dict = read_graph_in_dict(filename)
        self.graph = create_graph(self.graph_dict)

    def get_graph(self):
        return self.graph

    def bfs(self, root):
        """ Breadth-first search (BFS) algorithm"""
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
        """ Depth-first search (DFS) algorithm"""
        if visited is None:
            visited = []
        if root not in visited:
            visited.append(root)
            for next in self.graph_dict[root]:
                visited = self.dfs(next, visited)
        return visited

    def draw_graph_path_in_gif(self, vertexes, path):
        """ Visualisation path in graph"""
        draw_mode = Draw(self.graph)
        draw_mode.draw_path_gif(path, vertexes)
