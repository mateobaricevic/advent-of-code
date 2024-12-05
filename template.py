from argparse import ArgumentParser
from pathlib import Path

path = Path(__file__)
input_file = f'{path.parent}/inputs/{path.stem}.txt'

parser = ArgumentParser()
parser.add_argument('-i', '--input', default=input_file)
parser.add_argument('-p', '--part', type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    lines = input_file.read().splitlines()


def part_1():
    return 1


def part_2():
    return 2


if args.part == 1:
    print(part_1())
else:
    print(part_2())
