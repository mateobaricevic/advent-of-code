import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--part', type=int, choices=[1, 2], default=1)
args = parser.parse_args()


def part_1():
    possible = []
    for i in range(245182, 790572 + 1):
        possible.append(str(i))

    possible_1 = [number for number in possible if list(number) == sorted(number)]

    possible_2 = []
    for number in possible_1:
        for digit in number:
            count = number.count(digit)
            if count >= 2:
                possible_2.append(number)
                break

    return len(possible_2)


def part_2():
    possible = []
    for i in range(245182, 790572 + 1):
        possible.append(str(i))

    possible_1 = [number for number in possible if list(number) == sorted(number)]

    possible_2 = []
    for number in possible_1:
        for digit in number:
            count = number.count(digit)
            if count == 2:
                possible_2.append(number)
                break

    return len(possible_2)


if args.part == 1:
    print(part_1())
else:
    print(part_2())
