def readFromFile(instructionPath: str, tapePath: str) -> tuple[list[list[str]], str]:  # noqa 501
    with open(instructionPath) as fileHandle:
        lines = []
        for line in fileHandle:
            line.rstrip()
            line = line.split()
            lines.append(line)
    with open(tapePath) as fileHandle:
        tape = fileHandle.read()
        tape.rstrip()
    return (lines, tape)
