from dataclasses import dataclass
from graph import Graph


class WrongDataProvided(Exception):
    pass


@dataclass
class Dijkstra:
    graph: Graph
    source: int
    destination: int

    def __post_init__(self) -> None:
        if not isinstance(self.graph, Graph) or not isinstance(self.source, int) or not isinstance(self.destination, int):
            raise WrongDataProvided("Wrong data provided")

        sourceFound: bool = False
        destinationFound: bool = False
        for key, val in self.graph.content.items():
            if key == self.source:
                sourceFound = True
            if key == self.destination:
                destinationFound = True

        if not destinationFound or not sourceFound:
            raise WrongDataProvided("Wrong data provided")

    def minimumDistance(self, Distance, Q):
        min = float("inf")
        minIdx = None

        for v in Q:
            if Distance[v] < min:
                min = Distance[v]
                minIdx = v

        return minIdx

    def findShortestPath(self):
        length = self.graph.computeVertecies()

        Vertecies = list(self.graph.content.keys())              # All the vertecies of the graph
        Distance = [float("inf")] * length                       # Path cost table
        Predecessors = [-1] * length                             # Predeccessor table

        Distance[self.source] = 0

        actualVertecies = set(Vertecies)
        while actualVertecies:
            u = self.minimumDistance(actualVertecies)
            actualVertecies.remove(u)

            for item in self.graph.content[u]:
                v = item[0]
                weight = item[1]
                if Distance[v] > Distance[u] + weight:
                    Distance[v] = Distance[u] + weight
                    Predecessors[v] = u

        return Distance, Predecessors
