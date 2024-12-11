from argparse import ArgumentParser
from pathlib import Path

path = Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    line = input_file.read().splitlines()[0]
    stones = line.split(" ")
    stones = [int(stone) for stone in stones]
# print(stones)


def part_1():
    for _ in range(25):
        new_stones = []
        for i, stone in enumerate(stones):
            if stone == 0:
                stones[i] = 1
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                j = len(s) // 2
                left, right = int(s[:j]), int(s[j:])
                stones[i] = left
                new_stones.append((right, i + 1))
            else:
                stones[i] *= 2024

        for new_stone, i in reversed(new_stones):
            stones.insert(i, new_stone)
        # print(stones)

    return len(stones)


def part_2():
    def count_stones(stone, blinks, cache={}):
        if blinks == 0:
            return 1

        key = f"{stone},{blinks}"
        if key in cache:
            return cache[key]

        if stone == 0:
            result = count_stones(1, blinks - 1, cache)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            j = len(s) // 2
            left, right = int(s[:j]), int(s[j:])
            result = count_stones(left, blinks - 1, cache) + count_stones(right, blinks - 1, cache)
        else:
            result = count_stones(stone * 2024, blinks - 1, cache)

        cache[key] = result
        return result

    total = 0
    for stone in stones:
        total += count_stones(stone, 75)
    return total


if args.part == 1:
    print(part_1())
else:
    print(part_2())
