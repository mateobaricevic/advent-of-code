import argparse
import pathlib

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

with open(args.input) as input_file:
    grid = [list(line) for line in input_file.read().splitlines()]
    # pprint(map)


def part_1(grid: list):
    accessable = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            count = 0
            for k, l in neighbors:
                if 0 <= i + k < len(grid) and 0 <= j + l < len(grid):
                    if grid[i + k][j + l] == "@":
                        count += 1
                    # print(i, j, i + k, j + k, map[i + k][j + l], count)
                    if count == 4:
                        break
            if grid[i][j] == "@" and count < 4:
                accessable += 1
    return accessable


def part_2(grid: list):
    removed = 0
    while True:
        accessable = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                count = 0
                for k, l in neighbors:
                    if 0 <= i + k < len(grid) and 0 <= j + l < len(grid):
                        if grid[i + k][j + l] == "@":
                            count += 1
                        # print(i, j, i + k, j + k, map[i + k][j + l], count)
                        if count == 4:
                            break
                if grid[i][j] == "@" and count < 4:
                    accessable.append((i, j))
        for i, j in accessable:
            grid[i][j] = "."
            removed += 1
        if len(accessable) == 0:
            break
        # pprint(map)
    return removed


if args.part == 1:
    print(part_1(grid))
else:
    print(part_2(grid))
