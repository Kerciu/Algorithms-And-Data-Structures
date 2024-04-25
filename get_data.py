def read_from_file(path):
    array_of_lines = []
    with open(path) as file_handle:
        for line in file_handle:
            line = line.rstrip()
            array_of_lines.append(line)
    return array_of_lines
