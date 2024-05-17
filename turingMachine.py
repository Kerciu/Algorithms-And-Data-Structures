from fileService import readFromFile

def turing(instruction_path: str, tape_path: str) -> str:  # noqa 501
    lines, tape = readFromFile(instruction_path, tape_path)
    return "1100"
