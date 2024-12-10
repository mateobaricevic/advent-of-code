from argparse import ArgumentParser
from pathlib import Path

path = Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    map = input_file.read().splitlines()
# pprint(map)


directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def part_1():
    def explore(x, y, found):
        elevation = int(map[y][x])
        if elevation == 9:
            found.add((x, y))
            return

        for dx, dy in directions:
            if 0 <= y + dy < len(map) and 0 <= x + dx < len(map[y]):
                if map[y + dy][x + dx] == str(elevation + 1):
                    explore(x + dx, y + dy, found)

    score = 0
    for y, row in enumerate(map):
        for x, elevation in enumerate(row):
            if int(elevation) == 0:
                found = set()
                explore(x, y, found)
                score += len(found)
    return score


def part_2():
    def explore(x, y):
        elevation = int(map[y][x])
        if elevation == 9:
            return 1

        score = 0
        for dx, dy in directions:
            if 0 <= y + dy < len(map) and 0 <= x + dx < len(map[y]):
                if map[y + dy][x + dx] == str(elevation + 1):
                    score += explore(x + dx, y + dy)
        return score

    rating = 0
    for y, row in enumerate(map):
        for x, elevation in enumerate(row):
            if int(elevation) == 0:
                rating += explore(x, y)
    return rating


if args.part == 1:
    print(part_1())
else:
    print(part_2())
