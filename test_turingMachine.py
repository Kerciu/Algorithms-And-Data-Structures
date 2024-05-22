from turingMachine import Turing
from transitionFunction import TransitionFunction
from unittest.mock import MagicMock
import pytest


def test_initialization():
    transitions = [
        TransitionFunction('init', '1', '1', 'R', 'init'),
        TransitionFunction('init', '0', '0', 'R', 'init'),
        TransitionFunction('init', '_', '_', 'L', 'carry'),
        TransitionFunction('carry', '1', '0', 'L', 'carry'),
        TransitionFunction('carry', '0', '1', 'N', 'halt'),
        TransitionFunction('carry', '_', '1', 'N', 'halt'),
    ]
    tape = "1011"
    machine = Turing(transitions, tape)
    
    assert machine.tape == ['1', '0', '1', '1', '_']
    assert machine.head == 0
    assert machine.state == "init"


def test_take_step():
    transitions = [
        TransitionFunction('init', '1', '1', 'R', 'init'),
        TransitionFunction('init', '0', '0', 'R', 'init'),
        TransitionFunction('init', '_', '_', 'L', 'carry'),
        TransitionFunction('carry', '1', '0', 'L', 'carry'),
        TransitionFunction('carry', '0', '1', 'N', 'halt'),
        TransitionFunction('carry', '_', '1', 'N', 'halt'),
    ]
    tape = "1011"
    machine = Turing(transitions, tape)

    assert machine.state == "init"
    assert machine.head == 0
    assert machine.tape == ['1', '0', '1', '1', '_']

    machine.takeStep()
    assert machine.state == "init"
    assert machine.head == 1
    assert machine.tape == ['1', '0', '1', '1', '_']

    machine.takeStep()
    assert machine.state == "init"
    assert machine.head == 2
    assert machine.tape == ['1', '0', '1', '1', '_']


def test_run_machine():
    transitions = [
        TransitionFunction('init', '1', '1', 'R', 'init'),
        TransitionFunction('init', '0', '0', 'R', 'init'),
        TransitionFunction('init', '_', '_', 'L', 'carry'),
        TransitionFunction('carry', '1', '0', 'L', 'carry'),
        TransitionFunction('carry', '0', '1', 'N', 'halt'),
        TransitionFunction('carry', '_', '1', 'N', 'halt'),
    ]
    tape = "1011"
    machine = Turing(transitions, tape)

    machine.runMachine()

    # After running the machine, it should halt
    assert machine.state == "halt"
    assert machine.head == 1
    assert machine.tape == ['1', '1', '0', '0', '_']


@pytest.fixture
def mocker():
    return MagicMock()


def test_create_machine_from_file(mocker):
    mock_return_value = (
        [
            ['init', '1', '1', 'R', 'init'],
            ['init', '0', '0', 'R', 'init'],
            ['init', '_', '_', 'L', 'carry'],
            ['carry', '1', '0', 'L', 'carry'],
            ['carry', '0', '1', 'N', 'halt'],
            ['carry', '_', '1', 'N', 'halt'],
        ],
        "1011"
    )

    mocker.patch('fileService.readFromFile', return_value=mock_return_value)

    machine = Turing.createMachineFromFile('1011', 'instruction1.txt')

    assert machine.tape == ['1', '0', '1', '1', '_']
    assert machine.head == 0
    assert machine.state == "init"
    assert len(machine.transitions) == 2
    assert 'init' in machine.transitions
    assert 'carry' in machine.transitions
