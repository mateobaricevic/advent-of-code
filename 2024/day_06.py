from argparse import ArgumentParser
from pathlib import Path

path = Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

obstructions = []
guard = [-1, -1]
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                obstructions.append((x, y))
            elif char == "^":
                guard = [x, y]


def part_1():
    d = 0
    x, y = guard
    visited = set()
    while 0 <= y < len(lines) and 0 <= x < len(lines[y]):
        new_x = x + directions[d][0]
        new_y = y + directions[d][1]
        if (new_x, new_y) in obstructions:
            d += 1
            if d == len(directions):
                d = 0
            continue
        visited.add((x, y))
        x = new_x
        y = new_y

    return len(visited)


def part_2():
    d = 0
    x, y = guard
    visited = []
    while 0 <= y < len(lines) and 0 <= x < len(lines[y]):
        new_x = x + directions[d][0]
        new_y = y + directions[d][1]
        if (new_x, new_y) in obstructions:
            d += 1
            if d == len(directions):
                d = 0
            continue
        visited.append((x, y))
        x = new_x
        y = new_y

    results = set()
    for obstruction_x, obstruction_y in visited[1:]:
        new_obstructions = obstructions + [(obstruction_x, obstruction_y)]

        d = 0
        x, y = guard
        visited = set()
        while 0 <= y < len(lines) and 0 <= x < len(lines[y]):
            if (x, y, d) in visited:
                results.add((obstruction_x, obstruction_y))
                break

            new_x = x + directions[d][0]
            new_y = y + directions[d][1]
            if (new_x, new_y) in new_obstructions:
                d += 1
                if d == len(directions):
                    d = 0
                continue
            visited.add((x, y, d))
            x = new_x
            y = new_y
    return len(results)


if args.part == 1:
    print(part_1())
else:
    print(part_2())
