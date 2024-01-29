import argparse
import copy
import math
import pathlib
import re
from datetime import datetime

path = pathlib.Path(__file__)
input_file = f'{path.parent}/inputs/{path.stem}.txt'

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default=input_file)
parser.add_argument('-p', '--part', type=int, choices=[1, 2], default=1)
args = parser.parse_args()


def part_1():
    class Space3D:
        def __init__(self, x: int = 0, y: int = 0, z: int = 0):
            self.x = x
            self.y = y
            self.z = z

        def __repr__(self):
            return f'{{"x":{self.x}, "y":{self.y}, "z":{self.z}}}'

        def values(self):
            return [self.x, self.y, self.z]

    class Moon:
        def __init__(
            self, name: str = None, position: Space3D = Space3D(), velocity: Space3D = Space3D()
        ):
            self.name = name
            self.position = position
            self.velocity = velocity

        def __repr__(self):
            return (
                f'{{"name":"{self.name}", "position":{self.position}, "velocity":{self.velocity}}}'
            )

    moons = [Moon(name=name) for name in ['Io', 'Europa', 'Ganymede', 'Callisto']]

    with open(args.input) as input_file:
        lines = input_file.read().splitlines()
        for i, line in enumerate(lines):
            line = re.sub(r'(?![-,])\D', '', line).split(',')
            line = list(map(int, line))
            moons[i].position = Space3D(x=line[0], y=line[1], z=line[2])
        # print(moons)

    time = 0
    max_time = 1000
    while time <= max_time:
        # if time % 10 == 0:
        #     print(f'Step {time}:')
        #     for moon in moons:
        #         print(f'{moon.name}: p={moon.position}, v={moon.velocity}')

        if time == max_time:
            total_energy = 0
            for moon in moons:
                potential_energy = sum(map(abs, moon.position.values()))
                kinetic_energy = sum(map(abs, moon.velocity.values()))
                total_energy += potential_energy * kinetic_energy
            return total_energy

        for moon in moons:
            velocity = copy.deepcopy(moon.velocity)
            for moon_2 in moons:
                if moon.position.x > moon_2.position.x:
                    velocity.x -= 1
                elif moon.position.x < moon_2.position.x:
                    velocity.x += 1
                if moon.position.y > moon_2.position.y:
                    velocity.y -= 1
                elif moon.position.y < moon_2.position.y:
                    velocity.y += 1
                if moon.position.z > moon_2.position.z:
                    velocity.z -= 1
                elif moon.position.z < moon_2.position.z:
                    velocity.z += 1
            moon.velocity = velocity

        for i, moon in enumerate(moons):
            moons[i].position.x += moon.velocity.x
            moons[i].position.y += moon.velocity.y
            moons[i].position.z += moon.velocity.z

        time += 1


def part_2_max_optimized_using_dictionaries():
    moons = [
        {'velocity': [0, 0, 0]},
        {'velocity': [0, 0, 0]},
        {'velocity': [0, 0, 0]},
        {'velocity': [0, 0, 0]},
    ]
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    with open(args.input) as input_file:
        lines = input_file.read().splitlines()
        for i, line in enumerate(lines):
            line = re.sub(r'(?![-,])\D', '', line).split(',')
            line = list(map(int, line))
            moons[i]['position'] = [line[0], line[1], line[2]]
        # print(moons)

    time = 0
    initial_state = copy.deepcopy(moons)
    start_time = datetime.now()
    while True:
        if time % 100000 == 0:
            elapsed_time = datetime.now() - start_time
            print(f'{time:,.0f} ({elapsed_time})', end='\r')

        if time != 0:
            same_as_initial = True
            for moon_id, moon in enumerate(moons):
                if (
                    moon['position'][0] != initial_state[moon_id]['position'][0]
                    or moon['position'][1] != initial_state[moon_id]['position'][1]
                    or moon['position'][2] != initial_state[moon_id]['position'][2]
                    or moon['velocity'][0] != initial_state[moon_id]['velocity'][0]
                    or moon['velocity'][1] != initial_state[moon_id]['velocity'][1]
                    or moon['velocity'][2] != initial_state[moon_id]['velocity'][2]
                ):
                    same_as_initial = False
                    break
            if same_as_initial:
                print()
                return time + 1

        for moon, moon_2 in pairs:
            if moons[moon]['position'][0] > moons[moon_2]['position'][0]:
                moons[moon]['velocity'][0] -= 1
                moons[moon_2]['velocity'][0] += 1
            elif moons[moon]['position'][0] < moons[moon_2]['position'][0]:
                moons[moon]['velocity'][0] += 1
                moons[moon_2]['velocity'][0] -= 1

            if moons[moon]['position'][1] > moons[moon_2]['position'][1]:
                moons[moon]['velocity'][1] -= 1
                moons[moon_2]['velocity'][1] += 1
            elif moons[moon]['position'][1] < moons[moon_2]['position'][1]:
                moons[moon]['velocity'][1] += 1
                moons[moon_2]['velocity'][1] -= 1

            if moons[moon]['position'][2] > moons[moon_2]['position'][2]:
                moons[moon]['velocity'][2] -= 1
                moons[moon_2]['velocity'][2] += 1
            elif moons[moon]['position'][2] < moons[moon_2]['position'][2]:
                moons[moon]['velocity'][2] += 1
                moons[moon_2]['velocity'][2] -= 1

        for moon in moons:
            moon['position'][0] += moon['velocity'][0]
            moon['position'][1] += moon['velocity'][1]
            moon['position'][2] += moon['velocity'][2]

        time += 1


def part_2():
    moons = [
        {'velocity': [0, 0, 0]},
        {'velocity': [0, 0, 0]},
        {'velocity': [0, 0, 0]},
        {'velocity': [0, 0, 0]},
    ]
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    with open(args.input) as input_file:
        lines = input_file.read().splitlines()
        for i, line in enumerate(lines):
            line = re.sub(r'(?![-,])\D', '', line).split(',')
            line = list(map(int, line))
            moons[i]['position'] = [line[0], line[1], line[2]]
        # print(moons)

    initial_state = copy.deepcopy(moons)
    start_time = datetime.now()
    n = []
    # Find length of periods when each of the dimensions repeat
    # and then calculate least common multiple to get when all of them will align
    for i in [0, 1, 2]:
        time = 0
        while True:
            if time % 100000 == 0:
                elapsed_time = datetime.now() - start_time
                print(f'{time:,.0f} ({elapsed_time})', end='\r')

            if time != 0:
                same_as_initial = True
                for moon_id, moon in enumerate(moons):
                    if (
                        moon['position'][i] != initial_state[moon_id]['position'][i]
                        or moon['velocity'][i] != initial_state[moon_id]['velocity'][i]
                    ):
                        same_as_initial = False
                        break
                if same_as_initial:
                    print(f'\n{i}: {time + 1}')
                    n.append(time)
                    break

            for moon, moon_2 in pairs:
                if moons[moon]['position'][i] > moons[moon_2]['position'][i]:
                    moons[moon]['velocity'][i] -= 1
                    moons[moon_2]['velocity'][i] += 1
                elif moons[moon]['position'][i] < moons[moon_2]['position'][i]:
                    moons[moon]['velocity'][i] += 1
                    moons[moon_2]['velocity'][i] -= 1

            for moon in moons:
                moon['position'][i] += moon['velocity'][i]

            time += 1

    return math.lcm(*n)


if args.part == 1:
    print(part_1())
else:
    print(part_2())
