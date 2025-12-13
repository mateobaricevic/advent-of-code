import argparse
import pathlib

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    lines = input_file.read().split("\n\n")
    shapes = []
    regions = []
    for line in lines[:-1]:
        line = line.split("\n")
        shape_id = line[0][:-1]
        shape = [row for row in line[1:]]
        shapes.append(shape)
    for region in lines[-1].split("\n")[:-1]:
        region = region.split(": ")
        width, height = region[0].split("x")
        counts = [int(n) for n in region[1].split(" ")]
        regions.append((int(width), int(height), counts))
    # pprint(shapes)
    # pprint(regions)


def part_1(regions):
    answer = 0
    for w, h, counts in regions:
        answer += 1 if w * h >= sum(counts) * 9 else 0
    return answer


print(part_1(regions))
