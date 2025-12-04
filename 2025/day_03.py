import argparse
import pathlib

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    banks = input_file.read().splitlines()


def part_1(banks: list):
    max_ns = []
    for bank in banks:
        max_n = 0
        for i, a in enumerate(bank):
            for b in bank[i + 1 :]:
                n = int(a + b)
                if n > max_n:
                    max_n = n
        max_ns.append(max_n)
    return sum(max_ns)


def part_2(banks: list):
    max_ns = []
    for bank in banks:
        d = len(bank) - 12  # How many digits we must remove
        stack = []

        for digit in bank:
            while d > 0 and stack and stack[-1] < digit:
                stack.pop()
                d -= 1
            stack.append(digit)

        # If we still need to remove digits, remove from the end
        if d > 0:
            stack = stack[:-d]

        max_ns.append(int("".join(stack)))
    return sum(max_ns)


if args.part == 1:
    print(part_1(banks))
else:
    print(part_2(banks))
