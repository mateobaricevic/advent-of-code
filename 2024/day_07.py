from argparse import ArgumentParser
from itertools import product
from operator import add, mul
from pathlib import Path

path = Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

equations = []
with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    for line in lines:
        value, arguments = line.split(": ")
        arguments = arguments.split(" ")
        equations.append((int(value), [int(a) for a in arguments]))
# pprint(equations)


def part_1():
    calibration = 0
    operators = [add, mul]
    for value, arguments in equations:
        for operations in product(operators, repeat=len(arguments) - 1):
            args = arguments.copy()
            for i, operation in enumerate(operations):
                args[i + 1] = operation(args[i], args[i + 1])
            if args[-1] == value:
                calibration += value
                break
    return calibration


def part_2():
    calibration = 0
    operators = [add, mul, lambda x, y: int(str(x) + str(y))]
    for value, arguments in equations:
        for operations in product(operators, repeat=len(arguments) - 1):
            args = arguments.copy()
            for i, operation in enumerate(operations):
                args[i + 1] = operation(args[i], args[i + 1])
            if args[-1] == value:
                calibration += value
                break
    return calibration


if args.part == 1:
    print(part_1())
else:
    print(part_2())
