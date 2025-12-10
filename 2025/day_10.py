import argparse
import pathlib

import pulp

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    machines = []
    for line in lines:
        elements = [element[1:-1] for element in line.split(" ")]
        machines.append(
            {
                "lights": [1 if c == "#" else 0 for c in elements[0]],
                "buttons": [[int(x) for x in button.split(",")] for button in elements[1:-1]],
                "joltage": [int(x) for x in elements[-1].split(",")],
            }
        )
    # pprint(machines)


def part_1(machines):
    total = 0
    for machine in machines:
        buttons = machine["buttons"]
        lights = machine["lights"]

        problem = pulp.LpProblem("lights", pulp.LpMinimize)
        x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(len(buttons))]
        y = [pulp.LpVariable(f"y_{i}", lowBound=None, cat="Integer") for i in range(len(lights))]
        problem += pulp.lpSum(x)
        for i in range(len(lights)):
            problem += pulp.lpSum(x[j] for j, btn in enumerate(buttons) if i in btn) - 2 * y[i] == lights[i]
        problem.solve(pulp.PULP_CBC_CMD(msg=False))

        total += sum(int(v.value()) for v in x)
    return total


def part_2(machines):
    total = 0
    for machine in machines:
        buttons = machine["buttons"]
        joltage = machine["joltage"]

        problem = pulp.LpProblem("joltage", pulp.LpMinimize)
        x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(len(buttons))]
        problem += pulp.lpSum(x)
        for i in range(len(joltage)):
            problem += pulp.lpSum(x[j] for j, btn in enumerate(buttons) if i in btn) == joltage[i]
        problem.solve(pulp.PULP_CBC_CMD(msg=False))

        total += sum(int(v.value()) for v in x)
    return total


if args.part == 1:
    print(part_1(machines))
else:
    print(part_2(machines))
