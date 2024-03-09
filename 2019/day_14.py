import argparse
import pathlib
from datetime import datetime
from pprint import pprint

path = pathlib.Path(__file__)
input_file = f'{path.parent}/inputs/{path.stem}.txt'

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default=input_file)
parser.add_argument('-p', '--part', type=int, choices=[1, 2], default=1)
args = parser.parse_args()


reactions = {}
with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    for reaction in lines:
        left_side, right_side = reaction.split(' => ')
        amount, result = right_side.split(' ')
        reactions[result] = [
            int(amount),
            [
                [
                    int(element.split(' ')[0]),
                    element.split(' ')[1],
                ]
                for element in left_side.split(', ')
            ],
        ]
# pprint(reactions)


bucket = {chemical: 0 for chemical in reactions}
bucket['ORE'] = 0
ore_cost = 0


def construct(chemical):
    global ore_cost

    for amount, element in reactions[chemical][1]:
        if element == 'ORE':
            bucket[element] += amount
            ore_cost += amount
        else:
            while bucket[element] < amount:
                construct(element)
                bucket[element] += reactions[element][0]

        bucket[element] -= amount


# Remnant of my struggles (._.`)
def unpack_reactions():
    queue = []
    for element, reaction in reactions.items():
        if 'ORE' in str(reaction):
            queue.append(element)

    print(queue)
    while len(queue) > 0:
        el = queue.pop(0)
        print(el)
        print('-' * 32)
        for e, reaction in reactions.items():
            for element in reaction[1]:
                if element[1] == el:
                    element[0] /= reactions[el][0]
                    element[1] = reactions[el][1]
                    if e not in queue:
                        queue.append(e)
        pprint(reactions)
        print(queue)


def part_1():
    construct('FUEL')
    return ore_cost


def part_2():
    global ore_cost

    fuel = 0
    start_time = datetime.now()
    while ore_cost < 1000000000000:
        construct('FUEL')
        fuel += 1

    print(f'Elapsed time: {datetime.now() - start_time}')
    return fuel - 1


if args.part == 1:
    print(part_1())
else:
    print(part_2())
