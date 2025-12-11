import argparse
import pathlib
from functools import cache

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    devices = {}
    for line in lines:
        device, outputs = line.split(": ")
        devices[device] = outputs.split(" ")
    # pprint(devices)


def part_1(devices):
    start = "you"
    end = "out"

    stack = [(start, [])]
    count = 0
    while stack:
        device, path = stack.pop()
        if device == end:
            count += 1
            continue
        for output in devices[device]:
            stack.append((output, path + [output]))

    return count


def part_2(devices):
    @cache
    def traverse(start, end):
        if start == end:
            return 1
        if start == "out":
            return 0
        return sum([traverse(i, end) for i in devices[start]])

    a = traverse("svr", "fft")
    b = traverse("fft", "dac")
    c = traverse("dac", "out")
    return a * b * c


if args.part == 1:
    print(part_1(devices))
else:
    print(part_2(devices))
