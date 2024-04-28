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