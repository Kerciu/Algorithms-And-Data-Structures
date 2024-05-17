def read_from_file(instruction_path: str, tape_path: str) -> tuple[list[list[str]], str]:  # noqa 501
    with open(instruction_path) as file_handle:
        lines = []
        for line in file_handle:
            line.rstrip()
            line = line.split()
            lines.append(line)
    with open(tape_path) as file_handle:
        tape = file_handle.read()
        tape.rstrip()
    return (lines, tape)


data = read_from_file("instruction1.txt", "tape1.txt")
print(data[0])
print("\n")
print(data[1])
