import argparse
import pathlib
from collections import defaultdict, deque
from itertools import combinations, islice

import numpy

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
        x, y = [int(x) for x in line.split(",")]
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


def part_2_failed(tiles):
    def print2d(grid):
        for row in grid:
            for column in row:
                print("X" if column else ".", end="")
            print()

    xs = [x for x, _ in tiles]
    ys = [y for _, y in tiles]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = numpy.full((height, width), False)
    for x, y in tiles:
        grid[y - min_y][x - min_x] = True
    print2d(grid)

    n = len(tiles)
    for i in range(n):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % n]

        if x1 == x2:
            y_start, y_end = sorted([y1, y2])
            for y in range(y_start + 1, y_end):
                grid[y - min_y][x1 - min_x] = True
        else:
            x_start, x_end = sorted([x1, x2])
            for x in range(x_start + 1, x_end):
                grid[y1 - min_y][x - min_x] = True
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
                if x1 + (py - y1) * (x2 - x1) / (y2 - y1) >= px:
                    inside = not inside

        return inside

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if is_inside(x, y):
                grid[y - min_y][x - min_x] = True
    print2d(grid)

    max_area = 0
    i = 0
    n_combinations = len(list(combinations(tiles, 2)))
    for (x1, y1), (x2, y2) in combinations(tiles, 2):
        min_x, max_x = sorted([x1, x2])
        min_y, max_y = sorted([y1, y2])

        cache = defaultdict(lambda: False)
        ok = True
        x = min_x + 1
        while ok and x < max_x:
            if cache[f"{x},{y1}"] and not is_inside(x, y1):
                ok = False
                cache[f"{x},{y1}"] = True
            if cache[f"{x},{y2}"] and not is_inside(x, y2):
                ok = False
                cache[f"{x},{y2}"] = True
            x += 1
        y = min_y + 1
        while ok and y < max_y:
            if cache[f"{x1},{y}"] and not is_inside(x1, y):
                ok = False
                cache[f"{x1},{y}"] = True
            if cache[f"{x2},{y}"] and not is_inside(x2, y):
                ok = False
                cache[f"{x2},{y}"] = True
            y += 1
        if ok:
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            max_area = max(max_area, area)
        i += 1
        print(f"{i}/{n_combinations} ({i / n_combinations * 100:.2f}%)", end="\r")
    print()
    return max_area


def part_2(tiles):
    def sliding_window(iterable, n):
        iterator = iter(iterable)
        window = deque(islice(iterator, n - 1), maxlen=n)
        for x in iterator:
            window.append(x)
            yield tuple(window)

    def intersects(rect_corner1, rect_corner2, segments):
        # Normalize rectangle bounds
        rx1, ry1 = rect_corner1
        rx2, ry2 = rect_corner2
        min_x = min(rx1, rx2)
        max_x = max(rx1, rx2)
        min_y = min(ry1, ry2)
        max_y = max(ry1, ry2)

        for seg in segments:
            (sx1, sy1), (sx2, sy2) = seg

            if sx1 == sx2:  # Vertical segment
                x = sx1
                y_min_seg = min(sy1, sy2)
                y_max_seg = max(sy1, sy2)

                # Check if x is within rectangle's x-range and y-ranges overlap
                if min_x < x < max_x and max(y_min_seg, min_y) < min(y_max_seg, max_y):
                    return True

            elif sy1 == sy2:  # Horizontal segment
                y = sy1
                x_min_seg = min(sx1, sx2)
                x_max_seg = max(sx1, sx2)

                # Check if y is within rectangle's y-range and x-ranges overlap
                if min_y < y < max_y and max(x_min_seg, min_x) < min(x_max_seg, max_x):
                    return True

        return False

    def sq_size(a, b):
        return (1 + abs(a[0] - b[0])) * (1 + abs(a[1] - b[1]))

    candidates = []
    for square in combinations(tiles, 2):
        if not intersects(square[0], square[1], sliding_window(tiles, 2)):
            candidates.append(square)

    return max([sq_size(a, b) for (a, b) in candidates])


if args.part == 1:
    print(part_1(tiles))
else:
    print(part_2(tiles))
