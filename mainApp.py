from turingMachine import Turing
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SyntaxError("python3 <tape> <instructions file>")

    turing = Turing.createMachineFromFile(sys.argv[2], sys.argv[1])
    turing.runMachine()
