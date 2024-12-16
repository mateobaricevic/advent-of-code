from argparse import ArgumentParser
from pathlib import Path

path = Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()


def print_map():
    for row in map:
        for column in row:
            print(column, end="")
        print()


def swap(list: list, a: tuple, b: tuple):
    list[a[1]][a[0]], list[b[1]][b[0]] = list[b[1]][b[0]], list[a[1]][a[0]]


map = []
moves = []
with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    done = False
    for y, line in enumerate(lines):
        if len(line) == 0:
            done = True
            continue
        if not done:
            map.append([])
            for x, char in enumerate(line):
                if char == "@":
                    start = [x, y]
                map[y].append(char)
        else:
            for move in line:
                moves.append(move)
print_map()
# print(moves)
# print(start)
directions = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}


def part_1():
    x, y = start
    for move in moves:
        # print(move)
        dx, dy = directions[move]
        if map[y + dy][x + dx] == "#":
            continue
        if map[y + dy][x + dx] == ".":
            swap(map, (x, y), (x + dx, y + dy))
            x += dx
            y += dy
        elif map[y + dy][x + dx] == "O":
            i, j = x + 2 * dx, y + 2 * dy
            while True:
                if map[j][i] == ".":
                    swap(map, (i, j), (x + dx, y + dy))
                    swap(map, (x, y), (x + dx, y + dy))
                    x += dx
                    y += dy
                    break
                if map[j][i] == "#":
                    break
                i += dx
                j += dy
        # print_map()
    result = 0
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == "O":
                result += 100 * y + x
    return result


def part_2():
    x, y = start
    for move in moves:
        print(move)
        dx, dy = directions[move]
        if map[y + dy][x + dx] == "#":
            continue
        if map[y + dy][x + dx] == ".":
            swap(map, (x, y), (x + dx, y + dy))
            x += dx
            y += dy
        elif map[y + dy][x + dx] == "[":
            i, j = x + 2 * dx, y + 2 * dy
            while True:
                if map[j][i] == ".":
                    if move == ">":
                        k = 1
                        while i - k != x:
                            swap(map, (i - k + 1, j), (i - k, j))
                            k += 1
                        swap(map, (x + dx + k, y + dy), (x + dx, y + dy))
                        swap(map, (x, y), (x + dx, y + dy))
                    elif move == "^":
                        pass
                    elif move == "v":
                        pass
                    x += dx
                    y += dy
                    break
                if map[j][i] == "#":
                    break
                i += dx
                j += dy
        elif map[y + dy][x + dx] == "]":
            i, j = x + 2 * dx, y + 2 * dy
            while True:
                if map[j][i] == ".":
                    if move == "<":
                        k = 1
                        while i + k != x:
                            swap(map, (i + k - 1, j), (i + k, j))
                            k += 1
                        swap(map, (x + dx + k, y + dy), (x + dx, y + dy))
                        swap(map, (x, y), (x + dx, y + dy))
                    elif move == "^":
                        pass
                    elif move == "v":
                        pass
                    x += dx
                    y += dy
                    break
                if map[j][i] == "#":
                    break
                i += dx
                j += dy
        print_map()
        exit()
    result = 0
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == "O":
                result += 100 * y + x
    return result


if args.part == 1:
    print(part_1())
else:
    print(part_2())
