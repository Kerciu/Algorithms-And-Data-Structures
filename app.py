# -----------------------------------------------------------
#          Find shortest path between given X points
#              presented on a (x, y) axis logic
#         in a text file board using Dijkstra algorithm
# -----------------------------------------------------------
#                   Made by Kacper Gorski
#                 https://github.com/Kerciu
# -----------------------------------------------------------
#   How to use this:
#   1. Create txt file presenting map with two X points
#   2. Type in into cmd: python3 app.py <map.txt>
#   3. Script will show you the shortest path
# -----------------------------------------------------------

from argparse import ArgumentParser
from dijkstra import Dijkstra
from graphInstance import Graph
from programHandler import ProgramHandler

# -----------------------------------------------------------
#                       Parse Args
# -----------------------------------------------------------


def parseArgs():
    argParser = ArgumentParser()
    argParser.add_argument("name")
    args = argParser.parse_args()
    return args

# -----------------------------------------------------------
#                      Main Script
# -----------------------------------------------------------


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

# -----------------------------------------------------------