from argparse import ArgumentParser
from get_data import read_from_file, convertBoardToGraph


def parseArgs():
    argParser = ArgumentParser()
    argParser.add_argument("name")
    args = argParser.parse_args()
    return args


if __name__ == "__main__":
    args = parseArgs()
    data = read_from_file(args.name)
    print(data)
    graphData = convertBoardToGraph(data)
    print(graphData)
