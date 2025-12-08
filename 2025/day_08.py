import argparse
import pathlib
from collections import defaultdict
from itertools import combinations

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    points = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))


class DSU:  # Disjoint Set Union
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        return True


def part_1(points, k=1000):
    n = len(points)
    distances = []
    for i, j in combinations(range(n), 2):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        dz = points[i][2] - points[j][2]
        distances.append((dx**2 + dy**2 + dz**2, i, j))
    distances.sort()

    dsu = DSU(n)
    for _, i, j in distances[:k]:
        dsu.union(i, j)

    circuits = defaultdict(int)
    for i in range(n):
        circuits[dsu.find(i)] += 1

    sizes = sorted(circuits.values(), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def part_2(points):
    n = len(points)
    distances = []
    for i, j in combinations(range(n), 2):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        dz = points[i][2] - points[j][2]
        distances.append((dx**2 + dy**2 + dz**2, i, j))
    distances.sort()

    dsu = DSU(n)

    components = n
    last_pair = None
    for _, i, j in distances:
        if components == 0:
            break
        if dsu.find(i) != dsu.find(j):
            dsu.union(i, j)
            components -= 1
            last_pair = (i, j)

    i, j = last_pair
    return points[i][0] * points[j][0]


if args.part == 1:
    print(part_1(points))
else:
    print(part_2(points))
