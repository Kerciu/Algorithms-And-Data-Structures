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

    def showGraph(self, shortestPaths: dict = None) -> None:
        graph = nx.DiGraph()
        for vertex, edges in self.content.items():
            for edge in edges:
                graph.add_edge(vertex, edge[0], weight=edge[1])

        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold")
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, 'weight'))

        if shortestPaths:
            lastKey = list(shortestPaths.keys())[-1]
            path = shortestPaths[lastKey]["Path"]
            for i in range(len(path) - 1):
                nx.draw_networkx_edges(graph, pos, edgelist=[(path[i], path[i+1])], edge_color="red", width=2.0)

        plt.show()
