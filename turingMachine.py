from fileService import readFromFile
from dataclasses import dataclass
from transitionFunction import TransitionFunction


@dataclass
class Turing:
    transitions: dict[str, dict[str, TransitionFunction]]
    tape: str
    head: int
    state: str

    def __init__(self, transitions: list[TransitionFunction], tape: str) -> None:
        self.transitions = {}

        for func in transitions:
            if func.currentState not in self.transitions:
                self.transitions[func.currentState] = {}
            self.transitions[func.currentState][func.currentSymbol] = func

        self.tape = [*tape]
        self.head = 0
        self.state = "init"
