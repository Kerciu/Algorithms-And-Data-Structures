from dataclasses import dataclass


@dataclass
class TransitionFunction:
    currentState: str
    currentSymbol: str
    newSymbol: str
    direction: str
    newState: str
