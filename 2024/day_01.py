import argparse
import pathlib

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    list_1 = []
    list_2 = []
    for line in lines:
        line = line.split("   ")
        list_1.append(int(line[0]))
        list_2.append(int(line[1]))


def part_1(list_1: list, list_2: list):
    list_1.sort()
    list_2.sort()
    return sum([abs(x - y) for x, y in zip(list_1, list_2)])


def part_2(list_1: list, list_2: list):
    similarity = 0
    for n in list_1:
        similarity += n * list_2.count(n)
    return similarity


if args.part == 1:
    print(part_1(list_1, list_2))
else:
    print(part_2(list_1, list_2))
