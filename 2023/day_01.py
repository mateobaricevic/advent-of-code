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

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part_1(lines):
    result = 0
    for line in lines:
        no_digits = [char for char in line if char.isdigit()]
        result += int(no_digits[0] + no_digits[-1])
    return result


def part_2(lines):
    result = 0
    for line in lines:
        output = []
        while len(line) > 0:
            for digit, d in digits.items():
                if line.startswith(digit) or line.startswith(d):
                    output.append(d)
            line = line[1:]
        result += int(output[0] + output[-1])
    return result


if args.part == 1:
    print(part_1(lines))
else:
    print(part_2(lines))
