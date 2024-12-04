from argparse import ArgumentParser
from itertools import product
from pathlib import Path

path = Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()


with open(args.input) as input_file:
    puzzle = input_file.read().splitlines()
# pprint(puzzle)

word = "XMAS"

step = [-1, 0, 1]
directions = list(product(step, step))
directions.remove((0, 0))


def check(puzzle, word, start):
    result = 0
    for direction in directions:
        i = 1
        found = True
        x, y = start
        while i < len(word):
            x += direction[0]
            y += direction[1]

            if not (0 <= y < len(puzzle)) or not (0 <= x < len(puzzle[y])) or puzzle[y][x] != word[i]:
                found = False
                break

            i += 1
        if found:
            result += 1
    return result


def part_1():
    starts = []
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] == word[0]:
                starts.append((x, y))

    result = 0
    for start in starts:
        result += check(puzzle, word, start)
    return result


def check_2(puzzle, start):
    directions = [
        (-1, 1, 1, -1),  # /
        (-1, -1, 1, 1),  # \
    ]
    for direction in directions:
        x, y = start
        x_2, y_2 = start
        x += direction[0]
        y += direction[1]
        x_2 += direction[2]
        y_2 += direction[3]

        if not (0 <= y < len(puzzle) and 0 <= x < len(puzzle[y])) or not (
            0 <= y_2 < len(puzzle) and 0 <= x_2 < len(puzzle[y_2])
        ):
            return 0

        if not (puzzle[y][x] == "S" and puzzle[y_2][x_2] == "M" or puzzle[y][x] == "M" and puzzle[y_2][x_2] == "S"):
            return 0
    return 1


def part_2():
    starts = []
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] == "A":
                starts.append((x, y))

    result = 0
    for start in starts:
        result += check_2(puzzle, start)
    return result


if args.part == 1:
    print(part_1())
else:
    print(part_2())
