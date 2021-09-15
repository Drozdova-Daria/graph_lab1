import pytest

import networkx as nx
import collections
from graph_visualisation.graph import Graph

BFS = Graph.bfs
DFS = Graph.dfs


__test_graph_1 = "graph1.txt"
__test_graph_2 = "graph2.txt"

valid_graph = Graph(filename=__test_graph_1)
invalid_graph = Graph(filename=__test_graph_2)


def test_build_graph():
    """
    Test function for building graph1 from valid and invalid source files
    """
    assert valid_graph.get_graph() is not None
    assert invalid_graph.get_graph() != collections.defaultdict(list)


def test_bfs():
    """
    Test function for comparison of custom and networkx built-in functions of BFS
    """
    assert BFS(valid_graph, sorted(list(valid_graph.get_graph().nodes))[0]) == \
               list(nx.bfs_tree(valid_graph.get_graph(), sorted(list(valid_graph.get_graph().nodes))[0]))


def test_dfs():
    """
    Test function for comparison of custom and networkx built-in functions of DFS
    """
    assert DFS(valid_graph, sorted(list(valid_graph.get_graph().nodes))[0]) == \
               list(nx.dfs_preorder_nodes(valid_graph.get_graph(), sorted(list(valid_graph.get_graph().nodes))[0]))
