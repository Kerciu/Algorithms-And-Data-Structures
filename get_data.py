def read_from_file(path):
    try:
        with open(path) as file:
            data = [line.strip() for line in file.readlines()]
        return data
    except FileExistsError:
        raise FileExistsError("File does not exist")
    except FileNotFoundError:
        raise FileNotFoundError("File was not found")
    except Exception:
        raise Exception("Exception occured")


def createGraph(board):
    graph = {}

    rows = len(board)
    cols = len(board[0])

    def isValidPoint(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for i in range(rows):
        for j in range(cols):
            graph[(i, j)] = []
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = i + dx, j + dy
                if isValidPoint(nx, ny):
                    if board[nx][ny] == 'J' or board[nx][ny] == 'X':
                        cost = 0
                    else:
                        cost = int(board[nx][ny])
                    graph[(i, j)].append(((nx, ny), cost))

    return graph


def convertBoardToGraph(board: str) -> dict:
    # ["1234", "2345", "5312"]

    graph = {}
    for i, elem in enumerate(board):
        graph[i + 1] = []
        for j, char in enumerate(elem):
            if char != '0':
                if char.isdigit():
                    graph[i + 1].append((j + 1, int(char)))
                elif char == 'J':
                    graph[i + 1].append((j + 1, 0))
                elif char == 'X':
                    graph[i + 1].append((j + 1, char))
                else:
                    raise ValueError(f"Invalid character '{char}' in the board")
    return graph
