from turingMachine import turing


def test_turing1():
    instruction_path = "instruction1.txt"
    tape_path = "tape1.txt"
    result = turing(instruction_path, tape_path)
    correct_result = "1100"
    assert correct_result == result


def test_turing2():
    instruction_path = "instruction2.txt"
    tape_path = "tape2.txt"
    result = turing(instruction_path, tape_path)
    correct_result = "11111B"
    assert correct_result == result
