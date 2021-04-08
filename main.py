import networkx as nx
from graph import Graph

if __name__ == '__main__':
    graph_dist = {0: [1,2], 1: [2], 2: [3], 3: [1,2]}

    filename = 'data.txt'

    G = Graph(filename=filename)
    nx.draw_networkx(G.graph)
    vertexes = G.bfs('A')
    '''print(vertexes)
    for i in range(1, len(vertexes) + 1):
        print(vertexes[:i])'''
