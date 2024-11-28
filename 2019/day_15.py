import argparse
import json
import os
import pathlib
from collections import defaultdict

from genericpath import exists

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


with open(args.input) as input_file:
    program = input_file.read().split(",")
    program = list(map(int, program))
    # print(program)


def print_screen(screen):
    os.system("clear")
    xs = [int(coords.split(",")[0]) for coords in screen]
    ys = [int(coords.split(",")[1]) for coords in screen]
    max_x, max_y, min_x, min_y = max(xs), max(ys), min(xs), min(ys)
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            if f"{x},{y}" in screen:
                content = screen[f"{x},{y}"]
            else:
                content = "."
            print(content, end="")
        print()


def print_maze(maze, clear=False):
    if clear:
        os.system("clear")
    for row in maze:
        for column in row:
            print(column, end="")
        print()


def part_1(maze, start):
    def dfs(x, y, path_length=0):
        if maze[y][x] == "O":
            return path_length

        if not (0 <= x < len(maze) and 0 <= y < len(maze[0])) or maze[y][x] != " ":
            return False

        maze[y][x] = "."
        path_length += 1

        # print_maze(maze, clear=True)

        for dx, dy in directions:
            length = dfs(x + dx, y + dy, path_length)
            if length:
                return length

        return False

    return dfs(*start)


def part_2(maze):
    minutes = 0
    while True:
        # print_maze(maze, clear=True)

        if " " not in [column for row in maze for column in row]:
            break

        minutes += 1

        oxygen = []
        for y, row in enumerate(maze):
            for x, column in enumerate(row):
                if column == "O":
                    oxygen.append((x, y))

        for x, y in oxygen:
            for dx, dy in directions:
                if 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[y + dy][x + dx] == " ":
                    maze[y + dy][x + dx] = "O"

    return minutes


if not exists(f"data/{path.stem}.json"):
    screen = {}
    screen["0,0"] = "D"
    x, y = 0, 0
    last_action = 0
    direction = last_direction = 1

    memory = defaultdict(int)
    for address, value in enumerate(program):
        memory[address] = value

    instruction_pointer = 0
    relative_base = 0
    while True:
        operation = str(memory[instruction_pointer])
        while len(operation) < 5:
            operation = "0" + operation
        # print(operation)
        # print(memory)

        opcode = int(operation[3:])
        parameter_1_mode = int(operation[2])
        parameter_2_mode = int(operation[1])
        parameter_3_mode = int(operation[0])

        parameter_1 = memory[instruction_pointer + 1]
        parameter_2 = memory[instruction_pointer + 2]
        parameter_3 = memory[instruction_pointer + 3]

        if parameter_1_mode == 0:  # Position mode
            argument_1 = memory[parameter_1]
        elif parameter_1_mode == 1:  # Immediate mode
            argument_1 = parameter_1
        elif parameter_1_mode == 2:  # Relative mode
            argument_1 = memory[parameter_1 + relative_base]

        if parameter_2_mode == 0:  # Position mode
            argument_2 = memory[parameter_2]
        elif parameter_2_mode == 1:  # Immediate mode
            argument_2 = parameter_2
        elif parameter_2_mode == 2:  # Relative mode
            argument_2 = memory[parameter_2 + relative_base]

        if parameter_1_mode == 2:  # Relative mode
            parameter_1 += relative_base
        if parameter_2_mode == 2:  # Relative mode
            parameter_2 += relative_base
        if parameter_3_mode == 2:  # Relative mode
            parameter_3 += relative_base

        if opcode == 1:  # Addition
            memory[parameter_3] = argument_1 + argument_2
            instruction_pointer += 4
        elif opcode == 2:  # Multiplication
            memory[parameter_3] = argument_1 * argument_2
            instruction_pointer += 4
        elif opcode == 3:  # Input
            # Manual input
            # print_screen(screen)
            # key_press = ''
            # while key_press not in ['up', 'down', 'left', 'right', 12]:
            #     time.sleep(0.1)
            #     key_press = keyboard.read_key()
            # if key_press == 'up':
            #     direction = 1
            # elif key_press == 'down':
            #     direction = 2
            # elif key_press == 'left':
            #     direction = 3
            # elif key_press == 'right':
            #     direction = 4
            # elif key_press == 12:
            #     break

            # Automatic input (Hug the wall)
            if last_action == 0:
                if last_direction == 1:
                    direction = 4
                elif last_direction == 2:
                    direction = 3
                elif last_direction == 3:
                    direction = 1
                elif last_direction == 4:
                    direction = 2
                last_direction = direction
            elif last_action == 1:
                if x == 0 and y == 0:
                    break
                if last_direction == 1:
                    direction = 3
                elif last_direction == 2:
                    direction = 4
                elif last_direction == 3:
                    direction = 2
                elif last_direction == 4:
                    direction = 1
                last_direction = direction
            # time.sleep(0.1)
            # print_screen(screen)

            memory[parameter_1] = direction
            instruction_pointer += 2
        elif opcode == 4:  # Output
            if argument_1 == 0:  # Encountered wall
                if direction == 1:  # Up
                    screen[f"{x},{y-1}"] = "X"
                elif direction == 2:  # Down
                    screen[f"{x},{y+1}"] = "X"
                elif direction == 3:  # Left
                    screen[f"{x-1},{y}"] = "X"
                elif direction == 4:  # Right
                    screen[f"{x+1},{y}"] = "X"
            elif argument_1 == 1:  # Moved successfully
                if screen[f"{x},{y}"] != "O":
                    screen[f"{x},{y}"] = " "
                if direction == 1:  # Up
                    y -= 1
                elif direction == 2:  # Down
                    y += 1
                elif direction == 3:  # Left
                    x -= 1
                elif direction == 4:  # Right
                    x += 1
                screen[f"{x},{y}"] = "D"
            elif argument_1 == 2:  # Found oxygen system
                if direction == 1:  # Up
                    y -= 1
                elif direction == 2:  # Down
                    y += 1
                elif direction == 3:  # Left
                    x -= 1
                elif direction == 4:  # Right
                    x += 1
                screen[f"{x},{y}"] = "O"
            last_action = argument_1
            instruction_pointer += 2
        elif opcode == 5:  # Jump if true
            if argument_1 != 0:
                instruction_pointer = argument_2
            else:
                instruction_pointer += 3
        elif opcode == 6:  # Jump if false
            if argument_1 == 0:
                instruction_pointer = argument_2
            else:
                instruction_pointer += 3
        elif opcode == 7:  # Less than
            if argument_1 < argument_2:
                memory[parameter_3] = 1
            else:
                memory[parameter_3] = 0
            instruction_pointer += 4
        elif opcode == 8:  # Equals
            if argument_1 == argument_2:
                memory[parameter_3] = 1
            else:
                memory[parameter_3] = 0
            instruction_pointer += 4
        elif opcode == 9:  # Relative base offset
            relative_base += argument_1
            instruction_pointer += 2
        elif opcode == 99:  # Exit
            break
        else:  # Invalid opcode
            raise Exception(f"Encountered invalid opcode {opcode} at {instruction_pointer}!")

    xs = [int(coords.split(",")[0]) for coords in screen]
    ys = [int(coords.split(",")[1]) for coords in screen]
    max_x, max_y, min_x, min_y = max(xs), max(ys), min(xs), min(ys)
    dx, dy = abs(min_x), abs(min_y)
    start = (dx, dy)
    maze = [[" " for _ in range(max_x + dx + 1)] for _ in range(max_y + dy + 1)]
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if f"{x},{y}" not in screen or screen[f"{x},{y}"] == "X":
                maze[y + dy][x + dx] = "X"
            elif screen[f"{x},{y}"] == "O":
                maze[y + dy][x + dx] = "O"

    with open(f"data/{path.stem}.json", "w") as output_file:
        json.dump({"maze": maze, "start": start}, output_file, sort_keys=True, indent=4)
else:
    with open(f"data/{path.stem}.json") as input_file:
        data = json.load(input_file)
        maze = data["maze"]
        start = data["start"]

if args.part == 1:
    print(part_1(maze, start))
else:
    print(part_2(maze))
