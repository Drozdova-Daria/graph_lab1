# Graph visualisation class

import networkx as nx
from matplotlib import pyplot
import imageio
import os


def create_gif(path, file_type):
    """ Creating a gif file from images in a directory"""
    images = []
    gif_name = 'graph1.gif'
    for subdir, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(subdir, file)
            if file_path.endswith(file_type):
                images.append(imageio.imread(file_path))
    imageio.mimsave(path + gif_name, images, duration=1)


class Draw:
    """ Graph visualisation class"""

    def __init__(self):
        self.file_type = '.png'

    def draw_iter(self, graph, vertexes, path):
        """ Drawing a path step"""
        nodes = list(graph.nodes())
        colors_node = []
        for node in nodes:
            if node in vertexes:
                colors_node.append('red')
            else:
                colors_node.append('blue')
        nx.draw_circular(graph, node_color=colors_node, with_labels=True)
        pyplot.savefig(path + self.file_type)
        pyplot.clf()

    def draw_path_gif(self, graph, path, vertexes):
        """ Drawing graph path"""
        nx.draw_circular(graph, with_labels=True)
        pyplot.savefig(path + '0.png')
        for i in range(1, len(vertexes) + 1):
            self.draw_iter(graph, vertexes[:i], path + str(i))

        create_gif(path, self.file_type)
