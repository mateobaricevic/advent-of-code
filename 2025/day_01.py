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
    rotations = []
    for line in lines:
        rotations.append({"direction": line[0], "amount": int(line[1:])})

def part_1(rotations: list):
    position = 50
    password = 0
    for rotation in rotations:
        if rotation["direction"] == "L":
            position -= rotation["amount"]
            while position < 0:
                position += 100
        elif rotation["direction"] == "R":
            position += rotation["amount"]
            while position > 99:
                position -= 100
        # print(f"{rotation["direction"]}{rotation["amount"]}", position)
        if position == 0:
            password += 1
    return password


def part_2(rotations: list):
    position = 50
    password = 0
    for rotation in rotations:
        if rotation["direction"] == "L":
            amount = rotation["amount"]
            while amount > 0:
                if position == 0:
                    password += 1
                position -= 1
                amount -= 1
                if position == -1:
                    position = 99
        elif rotation["direction"] == "R":
            amount = rotation["amount"]
            while amount > 0:
                if position == 0:
                    password += 1
                position += 1
                amount -= 1
                if position == 100:
                    position = 0
        # print(f"{rotation["direction"]}{rotation["amount"]}", position, password)
    return password


if args.part == 1:
    print(part_1(rotations))
else:
    print(part_2(rotations))
