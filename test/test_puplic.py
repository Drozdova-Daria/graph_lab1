import pytest

from main import graph
import networkx as nx
from graph import Graph
BFS = Graph.bfs
DFS = Graph.dfs


__test_graph_1 = "graph1.txt"
__test_graph_2 = "graph2.txt"
__test_graph_3 = "graph3.txt"

graph1 = graph(__test_graph_1)
graph2 = graph(__test_graph_2)
graph3 = graph(__test_graph_3)

valid_graphs = [graph1, graph2]
invalid_graphs = [graph3]


def test_build_graph():
    """
    Test function for building graph from valid and invalid source files
    """
    for valid_graph in valid_graphs:
        assert valid_graph.get_graph() is not None
    for invalid_graph in invalid_graphs:
        assert invalid_graph.get_graph() is None


def test_drawing():
    """
    Test function for drawing valid and invalid graphs
    """
    for graph in valid_graphs + invalid_graphs:
        graph.draw(show=False)
    for valid_graph in valid_graphs:
        assert valid_graph.is_drawn_successfully() is True
    for invalid_graph in invalid_graphs:
        assert invalid_graph.is_drawn_successfully() is False


def test_BFS():
    """
    Test function for comparison of custom and networkx built-in functions of BFS
    """
    for valid_graph in valid_graphs:
        assert BFS(valid_graph.get_graph(), list(valid_graph.get_graph().nodes)[0]) == \
               [nodes for nodes in nx.bfs_tree(valid_graph.get_graph(), list(valid_graph.get_graph().nodes)[0])]


def test_DFS():
    """
    Test function for comparison of custom and networkx built-in functions of DFS
    """
    for valid_graph in valid_graphs:
        assert DFS(valid_graph.get_graph(), list(valid_graph.get_graph().nodes)[0]) == \
               [nodes for nodes in
                nx.dfs_preorder_nodes(valid_graph.get_graph(), list(valid_graph.get_graph().nodes)[0])]


def test_build_gif_bfs_only():
    """
    Test function for drawing gif-file with visualization of BFS algorithm only
    """
    for graph in valid_graphs + invalid_graphs:
        graph.build_gif("bfs")
    for valid_graph in valid_graphs:
        assert valid_graph.is_gif_built_successfully() is True
    for invalid_graph in invalid_graphs:
        assert invalid_graph.is_gif_built_successfully() is False


def test_build_gif_dfs_only():
    """
    Test function for drawing gif-file with visualization of DFS algorithm only
    """
    for graph in valid_graphs + invalid_graphs:
        graph.build_gif("dfs")
    for valid_graph in valid_graphs:
        assert valid_graph.is_gif_built_successfully() is True
    for invalid_graph in invalid_graphs:
        assert invalid_graph.is_gif_built_successfully() is False


def test_build_gif_dfs_bfs():
    """
    Test function for drawing gif-file with visualization of both BFS and DFS algorithms
    """
    for graph in valid_graphs + invalid_graphs:
        graph.build_gif("bfs", "dfs")
    for valid_graph in valid_graphs:
        assert valid_graph.is_gif_built_successfully() is True
    for invalid_graph in invalid_graphs:
        assert invalid_graph.is_gif_built_successfully() is False