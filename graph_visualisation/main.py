# Visualisation of BFS and DFS algorithms

from graph_visualisation.graph import Graph


if __name__ == '__main__':
    # Source graph in dict
    graph = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'G'], 'D': ['B', 'E', 'F'],
             'E': ['B', 'D'], 'F': ['D'], 'G': ['B', 'C']}

    # Directories for saving files
    path_dfs = './images_dfs/'
    path_bfs = './images_bfs/'

    # Starting point of the path
    point = 'A'

    # Building a graph based on given dict
    G = Graph(dict=graph)

    # Find the sequences of vertices of DFS and BFS algorithms
    dfs_vertexes = G.dfs(point)
    bfs_vertexes = G.bfs(point)

    # Creating a gif file with results
    G.draw_graph_path_in_gif(dfs_vertexes, path_dfs)
    G.draw_graph_path_in_gif(bfs_vertexes, path_bfs)
