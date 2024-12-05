from argparse import ArgumentParser
from pathlib import Path

path = Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

rules = []
updates = []
with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    for line in lines:
        if "|" in line:
            rules.append(line.split("|"))
        elif "," in line:
            updates.append(line.split(","))
# pprint(rules)
# pprint(updates)


def part_1():
    result = 0
    for update in updates:
        valid = True
        for rule in rules:
            if rule[1] in update:
                i = update.index(rule[1])
                if rule[0] in update[i:]:
                    valid = False
                    break
        if valid:
            result += int(update[len(update) // 2])
    return result


def fix(update):
    invalid = True
    while invalid:
        for rule in rules:
            if rule[1] in update:
                i = update.index(rule[1])
                if rule[0] in update[i:]:
                    j = update.index(rule[0])
                    update[i], update[j] = update[j], update[i]
                    invalid = True
                    break
                invalid = False
    return update


def part_2():
    result = 0
    for update in updates:
        valid = True
        for rule in rules:
            if rule[1] in update:
                i = update.index(rule[1])
                if rule[0] in update[i:]:
                    valid = False
                    break
        if not valid:
            fixed_update = fix(update)
            result += int(fixed_update[len(fixed_update) // 2])
    return result


if args.part == 1:
    print(part_1())
else:
    print(part_2())
