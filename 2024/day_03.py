import argparse
import pathlib
from re import findall

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    lines = input_file.read().splitlines()


def part_1():
    result = 0
    for line in lines:
        muls = findall(r"mul\(\d{1,3},\d{1,3}\)", line)
        for mul in muls:
            mul = mul[4 : len(mul) - 1]
            x, y = mul.split(",")
            result += int(x) * int(y)

    return result


mul = r"mul\(\d{1,3},\d{1,3}\)"
do = r"do\(\)"
dont = r"don't\(\)"

regex = r"|".join([mul, do, dont])


def part_2():
    result = 0
    enabled = True
    for line in lines:
        instructions = findall(regex, line)
        for instruction in instructions:
            if "mul(" in instruction:
                if enabled:
                    mul = instruction[4 : len(instruction) - 1]
                    x, y = mul.split(",")
                    result += int(x) * int(y)
            elif instruction == "don't()":
                enabled = False
            elif instruction == "do()":
                enabled = True

    return result


if args.part == 1:
    print(part_1())
else:
    print(part_2())
