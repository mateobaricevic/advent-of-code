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
    ranges = []
    ids = []
    switched = False
    for line in lines:
        if line == "":
            switched = True
            continue
        if switched:
            ids.append(int(line))
        else:
            ranges.append([int(n) for n in line.split("-")])
    # print(ranges)
    # print(ids)


def part_1(ranges: list, ids: list):
    fresh = 0
    for id in ids:
        for low, high in ranges:
            if low <= id <= high:
                fresh += 1
                break
    return fresh


def part_2(ranges: list):
    ranges = sorted(ranges)

    for i in range(len(ranges) - 1):
        if ranges[i][1] > ranges[i + 1][0]:
            ranges[i + 1][0] = ranges[i][1] + 1
    fresh = 0
    for low, high in ranges:
        if low < high:
            fresh += high - low + 1
    return fresh


if args.part == 1:
    print(part_1(ranges, ids))
else:
    print(part_2(ranges))
