from argparse import ArgumentParser
from pathlib import Path

path = Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()


with open(args.input) as input_file:
    compressed_disk = input_file.read().splitlines()[0]
# print(compressed_disk)


def part_1():
    disk = []
    for i, size in enumerate(compressed_disk):
        if i % 2 == 0:
            disk += [i // 2] * int(size)
        else:
            disk += ["."] * int(size)
    # print(disk)

    for i in range(len(disk) - 1, 0, -1):
        j = disk.index(".")
        if disk[i] != "." and i > j:
            disk[i], disk[j] = disk[j], disk[i]
    # print(disk)

    checksum = 0
    for i, value in enumerate(disk):
        if value != ".":
            checksum += i * value
    return checksum


def part_2():
    class Block:
        def __init__(self, id, location, size):
            self.id = id
            self.location = location
            self.size = size

    files: list[Block] = []
    spaces: list[Block] = []
    location = 0
    for i, size in enumerate(compressed_disk):
        if i % 2 == 0:
            files.append(Block(i // 2, location, int(size)))
        else:
            spaces.append(Block(None, location, int(size)))
        location += int(size)

    for file in reversed(files):
        for space in spaces:
            if space.location < file.location and space.size >= file.size:
                file.location = space.location
                space.location += file.size
                space.size -= file.size

                if space.size == 0:
                    spaces.remove(space)
                break

    files.sort(key=lambda file: file.location)

    checksum = 0
    for file in files:
        for i in range(file.size):
            checksum += (file.location + i) * file.id
    return checksum


if args.part == 1:
    print(part_1())
else:
    print(part_2())
