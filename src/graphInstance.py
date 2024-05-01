from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Graph:
    # graphDict = {(0, 0): [((0, 1), 1), ((1, 0), 1)]...
    #                            /\  go to (0,1) with the cost of 1
    #          or to (1, 0) with ||  a cost of 1
    content: Dict[tuple[int], List[tuple[tuple[int], int]]]

    def computeVertecies(self) -> int:
        return len(self.content)
