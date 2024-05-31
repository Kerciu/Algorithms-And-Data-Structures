def readFromFile(instructionPath: str, tape: str) -> tuple[list[list[str]], str]:  # noqa 501
    with open(instructionPath) as fileHandle:
        lines = []
        for line in fileHandle:
            line.rstrip()
            line = line.split()
            lines.append(line)
    
    return (lines, tape)
