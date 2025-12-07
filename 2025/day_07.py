import argparse
import pathlib
from collections import defaultdict
from math import floor

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    diagram = input_file.read().splitlines()
    diagram = [[c for c in line] for line in diagram]


def part_1(diagram: list):
    def simulate(start):
        current = {start}
        splits = 0
        while current:
            new = set()
            for row, column in current:
                if row + 1 == len(diagram):
                    continue
                if diagram[row + 1][column] in [".", "S"]:
                    new.add((row + 1, column))
                elif diagram[row + 1][column] == "^":
                    splits += 1
                    new.add((row + 1, column - 1))
                    new.add((row + 1, column + 1))
            current = new
        return splits

    return simulate((0, floor(len(diagram[0]) / 2)))


def part_2(diagram: list):
    def simulate(start):
        current = defaultdict(int)
        current[start] = 1
        total_exited = 0
        while current:
            new = defaultdict(int)
            for (row, column), count in current.items():
                if row + 1 == len(diagram):
                    total_exited += count
                    continue
                if diagram[row + 1][column] in [".", "S"]:
                    new[(row + 1, column)] += count
                elif diagram[row + 1][column] == "^":
                    new[(row + 1, column - 1)] += count
                    new[(row + 1, column + 1)] += count
                else:
                    total_exited += count
            current = new
        return total_exited

    return simulate((0, floor(len(diagram[0]) / 2)))


if args.part == 1:
    print(part_1(diagram))
else:
    print(part_2(diagram))
