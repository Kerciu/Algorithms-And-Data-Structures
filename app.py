from argparse import ArgumentParser
from dijkstra import Dijkstra
from graph import Graph
from get_data import ProgramHandler


def parseArgs():
    argParser = ArgumentParser()
    argParser.add_argument("name")
    args = argParser.parse_args()
    return args


if __name__ == "__main__":
    args = parseArgs()
    handler = ProgramHandler()
    boardData = handler.readFromFile(args.name)

    graphData = handler.createGraph(boardData)
    graph = Graph(graphData)

    dijkstra = Dijkstra(graph, (1, 2), (3, 2))
    result = dijkstra.findShortestPath()

    print(handler.createTextPath(boardData, result))
