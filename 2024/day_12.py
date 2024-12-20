from argparse import ArgumentParser
from pathlib import Path

import numpy

path = Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()


def print_2d(list):
    for row in list:
        for column in row:
            if column == 255:
                column = 1
            print(f"{abs(column):.0f}", end="")
        print()


with open(args.input) as input_file:
    farm = input_file.read().splitlines()
# print_2d(farm)


directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


class Region:
    def __init__(self, locations: list):
        self.locations = locations

    def area(self):
        return len(self.locations)

    def perimiter(self):
        perimiter = 0
        for x, y in self.locations:
            for dx, dy in directions:
                if (
                    not (0 <= y + dy < len(farm))
                    or not (0 <= x + dx < len(farm[y]))
                    or farm[y + dy][x + dx] != farm[y][x]
                ):
                    perimiter += 1
        return perimiter

    def sides(self):
        # image = numpy.zeros((len(farm) + 2, len(farm[0]) + 2), dtype=numpy.uint8)
        # for x, y in self.locations:
        #     image[y + 1][x + 1] = 255
        # image = cv2.resize(image, (len(image) * 2, len(image[0]) * 2), interpolation=cv2.INTER_AREA)
        # print_2d(image)
        # scores = cv2.cornerHarris(image, 1, 1, 1)
        # print()
        # print_2d(scores)
        # count = sum([1 if x < -1 else 0 for row in scores for x in row])
        # print(count)

        image = numpy.zeros((len(farm) + 2, len(farm[0]) + 2), dtype=numpy.uint8)
        for x, y in self.locations:
            image[y + 1][x + 1] = 1
        new_image = []
        for row in image:
            new_row = []
            for column in row:
                new_row.append(column)
                new_row.append(column)
            new_image.append(new_row)
            new_image.append(new_row)
        image = new_image
        # print_2d(image)

        filters = [
            [
                [0, 0, 0],
                [0, 1, 1],
                [0, 1, 1],
            ],
            [
                [1, 0, 0],
                [0, 1, 1],
                [0, 1, 1],
            ],
            [
                [1, 1, 1],
                [1, 0, 0],
                [1, 0, 0],
            ],
        ]

        corners = 0
        for filter in filters:
            for _ in range(4):
                count = 0
                filter = [list(row) for row in zip(*reversed(filter))]
                # print()
                # print_2d(filter)
                for y in range(1, len(image) - 1):
                    for x in range(1, len(image[y]) - 1):
                        # print()
                        test = True
                        for dy in range(-1, 2):
                            for dx in range(-1, 2):
                                # print(image[y + dy][x + dx], filter[dy + 1][dx + 1])
                                if image[y + dy][x + dx] != filter[dy + 1][dx + 1]:
                                    test = False
                                    break
                            else:
                                continue
                            break
                        if test:
                            # print((x, y))
                            count += 1
                # print(count)
                corners += count
        return corners

    def __repr__(self):
        d = {
            "locations": self.locations,
            "area": self.area(),
            "perimiter": self.perimiter(),
            "sides": self.sides(),
        }
        return str(d)


regions: list[Region] = []
visited = []


def populate_region(x, y):
    for dx, dy in directions:
        if (
            0 <= y + dy < len(farm)
            and 0 <= x + dx < len(farm[y])
            and (x + dx, y + dy) not in visited
            and farm[y + dy][x + dx] == farm[y][x]
        ):
            visited.append((x + dx, y + dy))
            regions[-1].locations.append((x + dx, y + dy))
            populate_region(x + dx, y + dy)


for y in range(len(farm)):
    for x in range(len(farm[y])):
        if (x, y) not in visited:
            visited.append((x, y))
            regions.append(Region(locations=[(x, y)]))
            populate_region(x, y)
# pprint(regions)


def part_1():
    result = 0
    for region in regions:
        result += region.area() * region.perimiter()
    return result


def part_2():
    result = 0
    for region in regions:
        result += region.area() * region.sides()
    return result


# 878054 - too high


if args.part == 1:
    print(part_1())
else:
    print(part_2())
