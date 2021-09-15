# Visualisation of BFS and DFS algorithms

from graph_visualisation.graph import Graph

import argparse


class CommandLineRun:
    default_input_file = 'graph.txt'
    default_method = 'BFS'
    methods = ['BFS', 'DFS']
    default_output_directory = './images/'

    @staticmethod
    def run_from_file(args):
        graph = CommandLineRun.create_graph(args.input_file)
        method = CommandLineRun.get_method(args.method)
        output_directory = CommandLineRun.get_output_directory(args.output_dir)

        path = CommandLineRun.get_path(args.point, graph, method)

        graph.draw_graph_path_in_gif(path, output_directory)

    @staticmethod
    def create_graph(input_file):
        if input_file:
            return Graph(filename=args.input_file)
        else:
            return Graph(filename=CommandLineRun.default_input_file)

    @staticmethod
    def get_method(method):
        if method:
            if method not in CommandLineRun.methods:
                raise Exception
            return method
        else:
            return CommandLineRun.default_method

    @staticmethod
    def get_path(point, graph, method):
        if point:
            start_point = point
        else:
            start_point = list(graph.graph.nodes())[0]
        if method == 'BFS':
            return graph.bfs(start_point)
        else:
            return graph.dfs(start_point)

    @staticmethod
    def get_output_directory(dir):
        if dir:
            return dir
        else:
            return CommandLineRun.default_output_directory


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_file', dest='input_file', help='path to the file with graph (default: "graph.txt")')
    parser.add_argument('--method', dest='method', help='choose method for run (default: BFS)')
    parser.add_argument('--point', dest='point', help='the point at which the walk begins '
                                                      '(default: the first vertex of the graph)')
    parser.add_argument('--output_dir', dest='output_dir', help='output_directory (default: "./images/"')

    args = parser.parse_args()

    CommandLineRun.run_from_file(args)

