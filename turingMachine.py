from dataclasses import dataclass
from transitionFunction import TransitionFunction


@dataclass
class Turing:
    # transitionsDict = {
    # 'init': {
    #     '1': TransitionFunction(currentState='init', currentSymbol='1', newSymbol='1', direction='R', newState='init'),
    #     '0': TransitionFunction(currentState='init', currentSymbol='0', newSymbol='0', direction='R', newState='init'),
    #     '_': TransitionFunction(currentState='init', currentSymbol='_', newSymbol='_', direction='L', newState='carry')
    # },
    # 'carry': {
    #     '1': TransitionFunction(currentState='carry', currentSymbol='1', newSymbol='0', direction='L', newState='carry'),
    #     '0': TransitionFunction(currentState='carry', currentSymbol='0', newSymbol='1', direction='*', newState='halt'),
    #     '_': TransitionFunction(currentState='carry', currentSymbol='_', newSymbol='1', direction='*', newState='halt')
    # }
    # }

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
