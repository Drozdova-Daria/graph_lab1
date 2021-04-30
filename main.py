import networkx as nx
from graph import Graph
from matplotlib import pyplot
import imageio
import os



def draw_iter(G, vertexes, path):
    nodes = list(G.nodes())
    colors_node = []
    for node in nodes:
        if node in vertexes:
            colors_node.append('red')
        else:
            colors_node.append('blue')
    nx.draw_circular(G, node_color=colors_node, with_labels=True)
    pyplot.savefig(path + '.png')


def create_gif(path):
    images = []
    for subdir, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(subdir, file)
            if file_path.endswith(".png"):
                images.append(imageio.imread(file_path))
    imageio.mimsave(path + 'graph.gif', images, duration=1)


if __name__ == '__main__':
    graph_dist = {0: [1,2], 1: [2], 2: [3], 3: [1,2]}
    graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': [], 'D': [], 'E': []}
    filename = 'data.txt'
    path = './images/'
    G = Graph(dict=graph)

    vertexes = list(G.dfs('A'))
    print(vertexes)
    G.draw_graph_path_in_gif(vertexes, path)
