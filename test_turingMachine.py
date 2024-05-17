from turingMachine import turing


# add 1 to number
def test_turing1():
    instruction_path = "instruction1.txt"
    tape_path = "tape1.txt"
    result = turing(instruction_path, tape_path)
    correct_result = "1100"
    assert correct_result == result


# change 0 to X and 1 to Y
def test_turing2():
    instruction_path = "instruction2.txt"
    tape_path = "tape2.txt"
    result = turing(instruction_path, tape_path)
    correct_result = "XYXYYX"
    assert correct_result == result


# delete 0 from the string
def test_turing3():
    instruction_path = "instruction3.txt"
    tape_path = "tape3.txt"
    result = turing(instruction_path, tape_path)
    correct_result = "11111"
    assert correct_result == result


def test_turing4():
    instruction_path = "instruction4.txt"
    tape_path = "tape4.txt"
    result = turing(instruction_path, tape_path)
    correct_result = "1"
    assert correct_result == result
