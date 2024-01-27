import argparse
import pathlib

path = pathlib.Path(__file__)
input_file = f'{path.parent}/inputs/{path.stem}.txt'

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default=input_file)
parser.add_argument('-p', '--part', type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    wires = input_file.read().splitlines()


def part_1():
    def get_grid(wire):
        grid = {}
        x = y = step = 0

        for move in wire.split(','):
            direction = move[0]
            distance = int(move[1:])

            direction_x = direction_y = 0
            if direction == 'U':
                direction_y = -1
            if direction == 'D':
                direction_y = 1
            if direction == 'L':
                direction_x = -1
            if direction == 'R':
                direction_x = 1

            for _ in range(distance):
                x += direction_x
                y += direction_y
                step += 1

                if (x, y) not in grid:
                    grid[(x, y)] = step

        return grid

    wire_1 = get_grid(wires[0])
    wire_2 = get_grid(wires[1])

    intersections = list(set(wire_1.keys()) & set(wire_2.keys()))

    distances = []
    for intersection in intersections:
        manhattan_distance = abs(intersection[0]) + abs(intersection[1])
        distances.append(manhattan_distance)

    return min(distances)


def part_2():
    def get_grid(wire):
        grid = {}
        x = y = step = 0

        for move in wire.split(','):
            direction = move[0]
            distance = int(move[1:])

            direction_x = direction_y = 0
            if direction == 'U':
                direction_y = -1
            if direction == 'D':
                direction_y = 1
            if direction == 'L':
                direction_x = -1
            if direction == 'R':
                direction_x = 1

            for _ in range(distance):
                x += direction_x
                y += direction_y
                step += 1

                if (x, y) not in grid:
                    grid[(x, y)] = step

        return grid

    wire_1 = get_grid(wires[0])
    wire_2 = get_grid(wires[1])

    intersections = list(set(wire_1.keys()) & set(wire_2.keys()))

    combined_steps = [wire_1[intersection] + wire_2[intersection] for intersection in intersections]

    return min(combined_steps)


if args.part == 1:
    print(part_1())
else:
    print(part_2())
