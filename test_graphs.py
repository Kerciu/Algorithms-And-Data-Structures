from graphInstance import Graph
from dijkstra import Dijkstra, WrongDataProvided
import pytest
from programHandler import ProgramHandler


sampleGraphData = {(0, 0): [(2, 3), (3, 1)],
                   (0, 1): [(3, 2)],
                   (1, 0): [(4, 5)],
                   (4, 0): [(1, 2)]}


def test_compute_vertices():
    graph = Graph(sampleGraphData)
    assert graph.computeVertecies() == 4


def test_dijkstra_initialization():
    graph = Graph(sampleGraphData)
    dijkstra = Dijkstra(graph, (1, 0), (4, 0))
    assert dijkstra.graph == graph
    assert dijkstra.source == (1, 0)
    assert dijkstra.destination == (4, 0)


def test_dijkstra_wrong_data():
    with pytest.raises(WrongDataProvided):
        graph = Graph({})
        Dijkstra(graph, 'A', 'B')


def test_dijkstra_wrong_vertices():
    with pytest.raises(WrongDataProvided):
        graph = Graph(sampleGraphData)
        Dijkstra(graph, 5, 6)

@pytest.fixture
def example_graph():
    graph_content = {
        (0, 0): [((0, 1), 1), ((1, 1), 2)],
        (0, 1): [((0, 0), 1), ((1, 1), 1), ((1, 0), 1)],
        (1, 0): [((0, 1), 1), ((1, 1), 1), ((2, 0), 1)],
        (1, 1): [((0, 0), 2), ((0, 1), 1), ((1, 0), 1), ((2, 0), 1), ((2, 1), 1)],
        (2, 0): [((1, 0), 1), ((1, 1), 1), ((2, 1), 1)],
        (2, 1): [((1, 1), 1), ((2, 0), 1)]
    }
    graph = Graph(graph_content)
    return graph


def test_correct_data(example_graph):
    source = (0, 0)
    destination = (1, 1)
    dijkstra = Dijkstra(example_graph, source, destination)
    assert isinstance(dijkstra, Dijkstra)


def test_wrong_data():
    with pytest.raises(WrongDataProvided):
        Dijkstra({}, (0, 0), (1, 1))


def test_no_data():
    with pytest.raises(WrongDataProvided):
        Dijkstra({}, (0, 0), (1, 1))


def test_invalid_source_destination(example_graph):
    source = (0, 0)
    destination = (5, 5)
    with pytest.raises(WrongDataProvided):
        Dijkstra(example_graph, source, destination)


def test_shortest_path(example_graph):
    source = (0, 0)
    destination = (2, 1)
    dijkstra = Dijkstra(example_graph, source, destination)
    result = dijkstra.findShortestPath()
    expected_path = [(0, 0), (1, 1), (2, 1)]
    expected_cost = 3
    assert result["Path"] == expected_path
    assert result["Cost"] == expected_cost


def test_read_from_file_existing_file(tmp_path):
    file_content = "1 2 3\n4 5 6\n7 8 9"
    file_path = tmp_path / "test.txt"
    with open(file_path, "w") as file:
        file.write(file_content)
    assert ProgramHandler.readFromFile(file_path) == ["1 2 3", "4 5 6", "7 8 9"]


def test_read_from_file_nonexistent_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        ProgramHandler.readFromFile(tmp_path / "nonexistent_file.txt")


def test_create_graph():
    board = ['J112J', '12X21', 'J041J', '12X11', 'J111J']
    expected_graph = {(0, 0): [((0, 1), 0), ((1, 0), 0)], (0, 1): [((0, 2), 1), ((0, 0), 0), ((1, 1), 2)], (0, 2): [((0, 3), 2), ((0, 1), 1), ((1, 2), 0)], (0, 3): [((0, 4), 0), ((0, 2), 1), ((1, 3), 2)], (0, 4): [((0, 3), 0), ((1, 4), 0)], (1, 0): [((1, 1), 2), ((2, 0), 0), ((0, 0), 0)], (1, 1): [((1, 2), 0), ((1, 0), 1), ((2, 1), 0), ((0, 1), 1)], (1, 2): [((1, 3), 2), ((1, 1), 2), ((2, 2), 4), ((0, 2), 1)], (1, 3): [((1, 4), 1), ((1, 2), 0), ((2, 3), 1), ((0, 3), 2)], (1, 4): [((1, 3), 2), ((2, 4), 0), ((0, 4), 0)], (2, 0): [((2, 1), 0), ((3, 0), 0), ((1, 0), 0)], (2, 1): [((2, 2), 4), ((2, 0), 0), ((3, 1), 2), ((1, 1), 2)], (2, 2): [((2, 3), 1), ((2, 1), 0), ((3, 2), 0), ((1, 2), 0)], (2, 3): [((2, 4), 0), ((2, 2), 4), ((3, 3), 1), ((1, 3), 2)], (2, 4): [((2, 3), 0), ((3, 4), 0), ((1, 4), 0)], (3, 0): [((3, 1), 2), ((4, 0), 0), ((2, 0), 0)], (3, 1): [((3, 2), 0), ((3, 0), 1), ((4, 1), 1), ((2, 1), 0)], (3, 2): [((3, 3), 1), ((3, 1), 2), ((4, 2), 1), ((2, 2), 4)], (3, 3): [((3, 4), 1), ((3, 2), 0), ((4, 3), 1), ((2, 3), 1)], (3, 4): [((3, 3), 1), ((4, 4), 0), ((2, 4), 0)], (4, 0): [((4, 1), 0), ((3, 0), 0)], (4, 1): [((4, 2), 1), ((4, 0), 0), ((3, 1), 2)], (4, 2): [((4, 3), 1), ((4, 1), 1), ((3, 2), 0)], (4, 3): [((4, 4), 0), ((4, 2), 1), ((3, 3), 1)], (4, 4): [((4, 3), 0), ((3, 4), 0)]}
    actual_graph = ProgramHandler.createGraph(board)

    sorted_expected_keys = sorted(expected_graph.keys())
    sorted_actual_keys = sorted(actual_graph.keys())

    assert sorted_actual_keys == sorted_expected_keys

    for key in sorted_expected_keys:
        sorted_expected_neighbors = sorted(expected_graph[key])
        sorted_actual_neighbors = sorted(actual_graph[key])
        assert sorted_actual_neighbors == sorted_expected_neighbors


def test_find_x_positions_valid():
    board = [
        'X0J',
        '000',
        '0XJ'
    ]
    assert ProgramHandler.findXpositions(board) == [(0, 0), (2, 1)]


def test_find_x_positions_invalid():
    board = [
        'X0JX',
        '000X',
        '0XJX'
    ]
    with pytest.raises(ValueError):
        ProgramHandler.findXpositions(board)
