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
    
    # K01:	S ← Ø	zbiór S ustawiamy jako pusty
    # K02:	Q ← wszystkie wierzchołki grafu	 
    # K03:	Utwórz n elementową tablicę d	tablica na koszty dojścia
    # K04:	Utwórz n elementową tablicę p	tablica poprzedników na ścieżkach
    # K05	Tablicę d wypełnij największą
    # wartością dodatnią	 
    # K06:	d [v] ← 0	koszt dojścia do samego siebie jest zawsze zerowy
    # K07:	Tablicę p wypełnij wartościami -1	-1 oznacza brak poprzednika
    # K08:	Dopóki Q zawiera wierzchołki,
    # wykonuj kroki K09…K12	 
    # K09:	Z Q do S przenieś wierzchołek u
    # o najmniejszym d [u]	 
    # K10:	Dla każdego sąsiada w wierzchołka u :
    # wykonuj kroki K11…K12	przeglądamy sąsiadów przeniesionego wierzchołka
    # K11:	Jeśli w nie jest w Q,
    # to następny obieg pętli K10	szukamy sąsiadów obecnych w Q
    # K12:	Jeśli d [w] > d [u ] + waga krawędzi u – w,
    # to:
    # d [w] ← d [u] + waga krawędzi u – w
    # p [w] ← u	sprawdzamy koszt dojścia. Jeśli mamy niższy, to modyfikujemy koszt i zmieniamy poprzednika w na u
    # K13:	Zakończ

    def minimumDistance(self, Distance):
        min = float("inf")

        for v in range(self.graph.computeVertecies()):
            if Distance[v] < min:
                min = Distance[v]
                minIdx = v

        return minIdx

    def findShortestPath(self):
        length = self.graph.computeVertecies()

        S = []
        Vertecies = list(self.graph.content.keys())              # All the vertecies of the graph
        Distance = [float("inf")] * length                       # Path cost table
        Predecessors = [-1] * length                             # Predeccessor table

        Distance[self.source] = 0
