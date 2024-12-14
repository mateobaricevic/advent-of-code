import os
from argparse import ArgumentParser
from pathlib import Path

from PIL import Image

path = Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()


class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __repr__(self):
        d = {
            "position": self.position,
            "velocity": self.velocity,
        }
        return str(d)


robots: list[Robot] = []
with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    for line in lines:
        position, velocity = line.split(" ")
        position = position.split("=")[1].split(",")
        velocity = velocity.split("=")[1].split(",")
        robots.append(
            Robot(
                position=[int(c) for c in position],
                velocity=[int(c) for c in velocity],
            )
        )
# pprint(robots)

max_x = max([r.position[0] for r in robots])
max_y = max([r.position[1] for r in robots])


def print_map(robots: list[Robot], clear=False):
    if clear:
        os.system("clear")
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            count = 0
            for robot in robots:
                if robot.position == [x, y]:
                    count += 1
            if count == 0:
                print(" ", end="")
            else:
                print("X", end="")
        print()


def part_1():
    for _ in range(100):
        for robot in robots:
            robot.position[0] += robot.velocity[0]
            robot.position[1] += robot.velocity[1]

            if robot.position[0] < 0:
                robot.position[0] += max_x + 1
            if robot.position[1] < 0:
                robot.position[1] += max_y + 1
            if robot.position[0] > max_x:
                robot.position[0] -= max_x + 1
            if robot.position[1] > max_y:
                robot.position[1] -= max_y + 1
    # print_map(robots)

    quadrants = [[] for _ in range(4)]
    for robot in robots:
        if robot.position[0] < max_x // 2 and robot.position[1] < max_y // 2:
            quadrants[0].append(robot)
        elif robot.position[0] > max_x // 2 and robot.position[1] < max_y // 2:
            quadrants[1].append(robot)
        elif robot.position[0] < max_x // 2 and robot.position[1] > max_y // 2:
            quadrants[2].append(robot)
        elif robot.position[0] > max_x // 2 and robot.position[1] > max_y // 2:
            quadrants[3].append(robot)

    result = 1
    for quadrant in quadrants:
        result *= len(quadrant)
    return result


def part_2():
    for i in range(1, max_x * max_y + 1):
        for robot in robots:
            robot.position[0] += robot.velocity[0]
            robot.position[1] += robot.velocity[1]

            if robot.position[0] < 0:
                robot.position[0] += max_x + 1
            if robot.position[1] < 0:
                robot.position[1] += max_y + 1
            if robot.position[0] > max_x:
                robot.position[0] -= max_x + 1
            if robot.position[1] > max_y:
                robot.position[1] -= max_y + 1

        data = []
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                pixel = (0, 0, 0)
                for robot in robots:
                    if robot.position == [x, y]:
                        pixel = (255, 255, 255)
                        break
                data.append(pixel)
        image = Image.new("RGB", (max_x + 1, max_y + 1), "white")
        image.putdata(data)
        image.save(f"{path.parent}/data/{path.stem}/{i}.png")
    return "Done."


if args.part == 1:
    print(part_1())
else:
    print(part_2())
