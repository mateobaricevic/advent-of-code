import argparse
import pathlib
from collections import defaultdict

path = pathlib.Path(__file__)
input_file = f'{path.parent}/inputs/{path.stem}.txt'

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default=input_file)
parser.add_argument('-p', '--part', type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    map_orbits = [orbit.split(')') for orbit in lines]
    # print(map_orbits)


def part_1():
    orbits = {}
    for orbit in map_orbits:
        if orbit[1] not in orbits.keys():
            orbits[orbit[1]] = {orbit[0]}
        else:
            orbits[orbit[1]].add(orbit[0])
    # print(orbits)

    changed = True
    while changed:
        changed = False

        for target_object, orbiting_objects in orbits.items():
            for orbiting_object in orbiting_objects:
                if orbiting_object in orbits.keys():
                    old_orbits = orbits[target_object].copy()
                    orbits[target_object] |= orbits[orbiting_object]
                    if orbits[target_object] != old_orbits:
                        changed = True
                    break
    # print(orbits)

    count = 0
    for _, orbiting_objects in orbits.items():
        count += len(orbiting_objects)

    return count


def part_2():
    graph = defaultdict(list)
    for orbit in map_orbits:
        graph[orbit[0]].append(orbit[1])
        graph[orbit[1]].append(orbit[0])
    # print(graph)

    def breadth_first_search(graph, start, goal):
        explored = []
        queue = [[start]]

        if start == goal:
            print('Start and goal node are the same!')
            return 0

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in explored:
                neighbours = graph[node]

                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    if neighbour == goal:
                        # print(f'Shortest path from {start} to {goal}: {new_path}')
                        return len(new_path)

                explored.append(node)

        print(f"{start} and {goal} nodes aren't connected!")
        return -1

    return breadth_first_search(graph, 'YOU', 'SAN') - 3


if args.part == 1:
    print(part_1())
else:
    print(part_2())
