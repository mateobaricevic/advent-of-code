from argparse import ArgumentParser
from itertools import combinations
from pathlib import Path

path = Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

antennas = {}
with open(args.input) as input_file:
    map = input_file.read().splitlines()
    max_y = len(map)
    max_x = len(map[0])
    for y, row in enumerate(map):
        for x, column in enumerate(row):
            if column != ".":
                if column not in antennas:
                    antennas[column] = []
                antennas[column].append((x, y))
# pprint(antennas)


def print_map(antinodes):
    for y, row in enumerate(map):
        for x, column in enumerate(row):
            if (x, y) in antinodes:
                print("#", end="")
            else:
                print(column, end="")
        print()


def part_1():
    antinodes = set()
    for _, locations in antennas.items():
        for a, b in combinations(locations, 2):
            distance = [a[0] - b[0], a[1] - b[1]]

            x = a[0] + distance[0]
            y = a[1] + distance[1]
            if 0 <= x < max_x and 0 <= y < max_y:
                antinodes.add((x, y))

            x = b[0] - distance[0]
            y = b[1] - distance[1]
            if 0 <= x < max_x and 0 <= y < max_y:
                antinodes.add((x, y))
    # print_map(antinodes)
    return len(antinodes)


def part_2():
    antinodes = set()
    for _, locations in antennas.items():
        for a, b in combinations(locations, 2):
            distance = [a[0] - b[0], a[1] - b[1]]
            antinodes.add((a[0], a[1]))
            antinodes.add((b[0], b[1]))

            i = 1
            x = a[0] + i * distance[0]
            y = a[1] + i * distance[1]
            while 0 <= x < max_x and 0 <= y < max_y:
                antinodes.add((x, y))
                i += 1
                x = a[0] + i * distance[0]
                y = a[1] + i * distance[1]

            i = 1
            x = b[0] - i * distance[0]
            y = b[1] - i * distance[1]
            while 0 <= x < max_x and 0 <= y < max_y:
                antinodes.add((x, y))
                i += 1
                x = b[0] - i * distance[0]
                y = b[1] - i * distance[1]
    # print_map(antinodes)
    return len(antinodes)


if args.part == 1:
    print(part_1())
else:
    print(part_2())
