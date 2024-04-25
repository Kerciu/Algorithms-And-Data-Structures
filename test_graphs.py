from graph import Graph
from dijkstra import Dijkstra, WrongDataProvided
import pytest

sampleGraphData = {1: [(2, 3), (3, 1)],
                   2: [(3, 2)],
                   3: [(4, 5)],
                   4: [(1, 2)]}


def test_compute_vertices():
    graph = Graph(sampleGraphData)
    assert graph.computeVertecies() == 4


def test_dijkstra_initialization():
    graph = Graph(sampleGraphData)
    dijkstra = Dijkstra(graph, 1, 4)
    assert dijkstra.graph == graph
    assert dijkstra.source == 1
    assert dijkstra.destination == 4


def test_dijkstra_wrong_data():
    with pytest.raises(WrongDataProvided):
        graph = Graph({})
        Dijkstra(graph, 'A', 'B')


def test_dijkstra_wrong_vertices():
    with pytest.raises(WrongDataProvided):
        graph = Graph(sampleGraphData)
        Dijkstra(graph, 5, 6)
