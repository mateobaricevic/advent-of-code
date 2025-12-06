import argparse
import pathlib

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()


def part_1():
    with open(args.input) as input_file:
        lines = input_file.read().splitlines()
        lines = [" ".join(line.split()) for line in lines]
        problems = [[] for _ in range(len(lines[0].split()))]
        for line in lines:
            for i, n in enumerate(line.split()):
                problems[i].append(n)

    results = []
    for problem in problems:
        operation = problem.pop()
        result = 0
        for n in problem:
            if operation == "+":
                result += int(n)
            elif operation == "*":
                if result == 0:
                    result = 1
                result *= int(n)
        results.append(result)
    return sum(results)


def part_2():
    with open(args.input) as input_file:
        lines = input_file.read().splitlines()
        problems = []
        digits = []
        for column in range(len(lines[0]) - 1, -1, -1):
            digit = ""
            operation = ""
            for row in range(len(lines)):
                if lines[row][column] in ["*", "+"]:
                    operation = lines[row][column]
                elif lines[row][column] != " ":
                    digit += lines[row][column]
            if digit != "":
                digits.append(digit)
            if operation != "":
                problems.append([int(digit) for digit in digits] + [operation])
                digits = []
        # print(problems)

    results = []
    for problem in problems:
        operation = problem.pop()
        result = 0
        for n in problem:
            if operation == "+":
                result += int(n)
            elif operation == "*":
                if result == 0:
                    result = 1
                result *= int(n)
        results.append(result)
    return sum(results)


if args.part == 1:
    print(part_1())
else:
    print(part_2())
