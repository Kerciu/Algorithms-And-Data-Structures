from argparse import ArgumentParser
from dijkstra import Dijkstra
from graphInstance import Graph
from programHandler import ProgramHandler


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

    xPos = handler.findXpositions(boardData)
    dijkstra = Dijkstra(graph, xPos[0], xPos[1])
    result = dijkstra.findShortestPath()

    print(handler.createTextPath(boardData, result))
