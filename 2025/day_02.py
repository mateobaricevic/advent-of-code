import argparse
import pathlib
import re

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    ranges = input_file.read().splitlines()[0].split(",")
    ranges = [r.split("-") for r in ranges]
    ids = []
    for r in ranges:
        for i in range(int(r[0]), int(r[1]) + 1):
            ids.append(i)


def part_1(ids: list):
    pattern = re.compile(r"^(\d+)\1$")
    invalid_ids = []
    for id in ids:
        invalid = bool(pattern.match(str(id)))
        if invalid:
            invalid_ids.append(id)
    return sum(invalid_ids)


def part_2(ids: list):
    pattern = re.compile(r"^(\d+)\1+$")
    invalid_ids = []
    for id in ids:
        invalid = bool(pattern.match(str(id)))
        if invalid:
            invalid_ids.append(id)
    return sum(invalid_ids)


if args.part == 1:
    print(part_1(ids))
else:
    print(part_2(ids))
