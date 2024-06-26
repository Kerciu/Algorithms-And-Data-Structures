from dataclasses import dataclass
from graphInstance import Graph


class WrongDataProvided(Exception):
    pass


@dataclass
class Dijkstra:
    graph: Graph
    source: tuple[int]
    destination: tuple[int]
    # destination: tuple[int]

    def __post_init__(self) -> None:
        if not isinstance(self.graph, Graph) or not isinstance(self.source, tuple) or not isinstance(self.destination, tuple):
            raise WrongDataProvided("Wrong data provided")

        sourceFound: bool = False
        destinationFound: bool = False
        for key, val in self.graph.content.items():
            if key == self.source:
                sourceFound = True
            if key == self.destination:
                destinationFound = True

        if not sourceFound or not destinationFound:
            raise WrongDataProvided("No data provided")

    def _prettifyOutput(self, Distance: dict, Predecessors: dict) -> dict:
        pathThrough = []
        pathStart = self.destination

        while pathStart != self.source:
            pathThrough.append(pathStart)
            pathStart = Predecessors[pathStart]
        pathThrough.append(self.source)
        pathThrough.reverse()

        return {"Path": pathThrough, "Cost": Distance[self.destination]}

    def findShortestPath(self) -> dict:
        """
        Returns dictionary of costs to each
        """
        visited = set()
        distances = {(x, y): float('inf') for (x, y) in self.graph.content.keys()}
        distances[self.source] = 0
        predecessors = {(x, y): None for (x, y) in self.graph.content.keys()}

        currentVertex = self.source

        while len(visited) != len(distances):
            currentVertex = min(((x, y) for (x, y) in self.graph.content.keys() if (x, y) not in visited), key=lambda z: distances[z])
            visited.add(currentVertex)

            for neighbor_data in self.graph.content[currentVertex]:
                neighborPosition = neighbor_data[0]
                neightWeight = neighbor_data[1]
                distance = distances[currentVertex] + neightWeight

                if distance < distances[neighborPosition]:
                    distances[neighborPosition] = distance
                    predecessors[neighborPosition] = currentVertex

        return self._prettifyOutput(distances, predecessors)
