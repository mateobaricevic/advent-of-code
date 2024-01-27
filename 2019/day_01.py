import argparse
import pathlib

path = pathlib.Path(__file__)
input_file = f'{path.parent}/inputs/{path.stem}.txt'

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default=input_file)
parser.add_argument('-p', '--part', type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    modules = list(map(int, lines))
    # print(modules)


def part_1():
    fuels = []
    for module in modules:
        fuel = module // 3 - 2
        fuels.append(fuel)

    return sum(fuels)


def part_2():
    fuels = []
    for module in modules:
        fuel = module // 3 - 2
        fuels.append(fuel)
        while fuel > 0:
            fuel = fuel // 3 - 2
            if fuel > 0:
                fuels.append(fuel)

    return sum(fuels)


if args.part == 1:
    print(part_1())
else:
    print(part_2())
