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

    def _minimumDistance(self, Distance, Q):
        minDistance = float("inf")
        minIdx = None

        for v in Q:
            if Distance[v - 1] < minDistance:
                minDistance = Distance[v - 1]
                minIdx = v

        return minIdx

    def _prettifyOutput(self, Distance, Predecessors, length):
        shortestPaths = {}
        for i in range(length):
            vertex = i + 1
            path = []

            while vertex != -1:
                path.append(vertex)
                vertex = Predecessors[vertex - 1]
     
            path.reverse()
            shortestPaths[i + 1] = {"Path": path, "Cost": Distance[i]}

        return shortestPaths

    def findShortestPath(self):
        """
        Returns dictionary of costs to each 
        """
        length = self.graph.computeVertecies()
        Vertecies = list(self.graph.content.keys())              # All the vertecies of the graph
        Distance = [float("inf")] * length                       # Path cost table
        Predecessors = [-1] * length                             # Predeccessor table

        Distance[self.source - 1] = 0
        actualVertecies = set(Vertecies)

        while actualVertecies:

            u = self._minimumDistance(Distance, actualVertecies)
            actualVertecies.remove(u)

            for v, weight in self.graph.content[u]:

                if Distance[v - 1] > Distance[u - 1] + weight:
                    Distance[v - 1] = Distance[u - 1] + weight
                    Predecessors[v - 1] = u

        return self._prettifyOutput(Distance, Predecessors, length)


if __name__ == "__main__":
    dataGraph = {
        1: [(2, 10), (3, 15), (4, 20)],
        2: [(5, 25)],
        3: [(6, 5)],
        4: [(7, 10)],
        5: [(8, 15)],
        6: [(8, 20)],
        7: [(8, 25)],
        8: []
        }
    graph = Graph(dataGraph)
    graph.showGraph()
    pathFinder = Dijkstra(graph, 1, 4)

    shortest = pathFinder.findShortestPath()
    graph.showGraph(shortest)
