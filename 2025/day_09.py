import argparse
import pathlib

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    tiles = []
    for line in lines:
        x, y = map(int, line.split(","))
        tiles.append((x, y))


def part_1(tiles):
    max_area = 0
    n = len(tiles)

    for i in range(n):
        x1, y1 = tiles[i]
        for j in range(i + 1, n):
            x2, y2 = tiles[j]

            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height

            if area > max_area:
                max_area = area

    return max_area


def print2d(grid):
    for row in grid:
        for column in row:
            print(column, end="")
        print()


def part_2_not_optimized(tiles):
    xs = [x for x, y in tiles]
    ys = [y for x, y in tiles]
    min_x, max_x = min(xs) - 1, max(xs) + 1
    min_y, max_y = min(ys) - 1, max(ys) + 1

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = [["."] * width for _ in range(height)]
    for x, y in tiles:
        grid[y - min_y][x - min_x] = "#"
    # print2d(grid)

    n = len(tiles)
    for i in range(n):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % n]

        if x1 == x2:
            y_start, y_end = sorted([y1, y2])
            for y in range(y_start + 1, y_end):
                grid[y - min_y][x1 - min_x] = "#"
        else:
            x_start, x_end = sorted([x1, x2])
            for x in range(x_start + 1, x_end):
                grid[y1 - min_y][x - min_x] = "#"
    print2d(grid)

    def is_inside(px, py):
        inside = False
        n = len(tiles)

        for i in range(n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[(i + 1) % n]

            if y1 == y2:
                if py == y1 and min(x1, x2) <= px <= max(x1, x2):
                    return True
            if x1 == x2:
                if px == x1 and min(y1, y2) <= py <= max(y1, y2):
                    return True

            # Ray-casting
            if (y1 > py) != (y2 > py):
                if x1 + (py - y1) * (x2 - x1) / (y2 - y1) > px:
                    inside = not inside

        return inside

    inside = []
    for y in range(height):
        for x in range(width):
            if is_inside(x + 1, y):
                inside.append((x, y))
    for x, y in inside:
        grid[y][x] = "X"
    print2d(grid)

    max_area = 0
    for i in range(len(tiles)):
        x1, y1 = tiles[i]
        for j in range(i + 1, len(tiles)):
            x2, y2 = tiles[j]

            min_x, max_x = sorted([x1, x2])
            min_y, max_y = sorted([y1, y2])

            ok = True
            for yy in range(min_y, max_y + 1):
                for xx in range(min_x, max_x + 1):
                    if grid[yy][xx] == ".":
                        ok = False
                        break
                if not ok:
                    break

            if ok:
                area = (max_x - min_x + 1) * (max_y - min_y + 1)
                max_area = max(max_area, area)
    return max_area


# 4650952673 too high
# 4599100062 too high


def part_2(tiles):
    def is_inside(px, py):
        inside = False
        n = len(tiles)

        for i in range(n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[(i + 1) % n]

            if y1 == y2:
                if py == y1 and min(x1, x2) <= px <= max(x1, x2):
                    return True
            if x1 == x2:
                if px == x1 and min(y1, y2) <= py <= max(y1, y2):
                    return True

            # Ray-casting
            if (y1 > py) != (y2 > py):
                if x1 + (py - y1) * (x2 - x1) / (y2 - y1) > px:
                    inside = not inside

        return inside

    n = len(tiles)
    max_area = 0

    for i in range(n):
        x1, y1 = tiles[i]
        for j in range(i + 1, n):
            x2, y2 = tiles[j]

            if x1 == x2 or y1 == y2:
                continue

            min_x, max_x = sorted([x1, x2])
            min_y, max_y = sorted([y1, y2])

            if (
                is_inside(min_x + 1, min_y)
                and is_inside(min_x + 1, max_y)
                and is_inside(max_x + 1, min_y)
                and is_inside(max_x + 1, max_y)
            ):
                area = (max_x - min_x + 1) * (max_y - min_y + 1)
                max_area = max(max_area, area)

    return max_area


if args.part == 1:
    print(part_1(tiles))
else:
    print(part_2(tiles))
