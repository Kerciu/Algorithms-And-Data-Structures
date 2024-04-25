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
