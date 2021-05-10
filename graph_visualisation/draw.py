# Graph visualisation class

import networkx as nx
from matplotlib import pyplot
import imageio
import os


def create_gif(path):
    """ Creating a gif file from images in a directory"""
    images = []
    for subdir, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(subdir, file)
            if file_path.endswith(".png"):
                images.append(imageio.imread(file_path))
    imageio.mimsave(path + 'graph1.gif', images, duration=1)


class Draw:
    """ Graph visualisation class"""

    def __init__(self, graph):
        self.graph = graph

    def draw_iter(self, vertexes, path):
        """ Drawing a path step"""
        nodes = list(self.graph.nodes())
        colors_node = []
        for node in nodes:
            if node in vertexes:
                colors_node.append('red')
            else:
                colors_node.append('blue')
        nx.draw_circular(self.graph, node_color=colors_node, with_labels=True)
        pyplot.savefig(path + '.png')
        pyplot.clf()

    def draw_path_gif(self, path, vertexes):
        """ Drawing graph path"""
        nx.draw_circular(self.graph, with_labels=True)
        pyplot.savefig(path + '0.png')
        for i in range(1, len(vertexes) + 1):
            self.draw_iter(vertexes[:i], path + str(i))

        create_gif(path)
