from dataclasses import dataclass
from matplotlib import pyplot as plt
from typing import List, Dict
import networkx as nx


@dataclass
class Graph:
    # graphDict = {1 : [(2, 3), (3, 1)]}
    # From one     /\  go to 2 with the cost of 3
    # or to 3 with ||  a cost of 1
    content: Dict[int, List[tuple]]

    def computeVertecies(self) -> int:
        return len(self.content)

    def showGraph(self) -> None:
        graph = nx.DiGraph()
        for vertex, edges in self.content.items():
            for edge in edges:
                graph.add_edge(vertex, edge[0], weight=edge[1])

        pos = nx.spring_layout(graph)  # Określamy układ wierzchołków
        nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold")
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, 'weight'))
        plt.show()


if __name__ == "__main__":
    graphData = {
                1: [(2, 3), (3, 1)],
                2: [(3, 2)],
                3: [(4, 5)],
                4: [(1, 2)]}

    graph = Graph(graphData)
    graph.showGraph()
