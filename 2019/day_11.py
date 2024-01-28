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
    program = input_file.read().split(',')
    program = list(map(int, program))
    # print(program)


def part_1():
    memory = defaultdict(int)
    for address, value in enumerate(program):
        memory[address] = value

    instruction_pointer = 0
    relative_base = 0
    repainted_panels = set()
    painted_panels = set()
    x, y = 0, 0
    direction = 0
    mode = 'paint'
    while True:
        operation = str(memory[instruction_pointer])
        while len(operation) < 5:
            operation = '0' + operation
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
            memory[parameter_1] = 1 if f'{x},{y}' in painted_panels else 0
            instruction_pointer += 2
        elif opcode == 4:  # Output
            if mode == 'paint':
                if argument_1 == 0:  # Paint black
                    if f'{x},{y}' in painted_panels:
                        repainted_panels.add(f'{x},{y}')
                        painted_panels.remove(f'{x},{y}')
                elif argument_1 == 1:  # Paint white
                    painted_panels.add(f'{x},{y}')
                mode = 'turn'
            elif mode == 'turn':
                if argument_1 == 0:  # Turn left
                    if direction == 0:
                        direction = 1
                        x -= 1
                    elif direction == 1:
                        direction = 2
                        y += 1
                    elif direction == 2:
                        direction = 3
                        x += 1
                    elif direction == 3:
                        direction = 0
                        y -= 1
                elif argument_1 == 1:  # Turn right
                    if direction == 0:
                        direction = 3
                        x += 1
                    elif direction == 1:
                        direction = 0
                        y -= 1
                    elif direction == 2:
                        direction = 1
                        x -= 1
                    elif direction == 3:
                        direction = 2
                        y += 1
                mode = 'paint'
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
            raise Exception(f'Encountered invalid opcode {opcode} at {instruction_pointer}!')

    return len({*painted_panels, *repainted_panels})


def part_2():
    memory = defaultdict(int)
    for address, value in enumerate(program):
        memory[address] = value

    instruction_pointer = 0
    relative_base = 0
    repainted_panels = set()
    painted_panels = {'0,0'}
    x, y = 0, 0
    direction = 0
    mode = 'paint'
    while True:
        operation = str(memory[instruction_pointer])
        while len(operation) < 5:
            operation = '0' + operation
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
            memory[parameter_1] = 1 if f'{x},{y}' in painted_panels else 0
            instruction_pointer += 2
        elif opcode == 4:  # Output
            if mode == 'paint':
                if argument_1 == 0:  # Paint black
                    if f'{x},{y}' in painted_panels:
                        repainted_panels.add(f'{x},{y}')
                        painted_panels.remove(f'{x},{y}')
                elif argument_1 == 1:  # Paint white
                    painted_panels.add(f'{x},{y}')
                mode = 'turn'
            elif mode == 'turn':
                if argument_1 == 0:  # Turn left
                    if direction == 0:
                        direction = 1
                        x -= 1
                    elif direction == 1:
                        direction = 2
                        y += 1
                    elif direction == 2:
                        direction = 3
                        x += 1
                    elif direction == 3:
                        direction = 0
                        y -= 1
                elif argument_1 == 1:  # Turn right
                    if direction == 0:
                        direction = 3
                        x += 1
                    elif direction == 1:
                        direction = 0
                        y -= 1
                    elif direction == 2:
                        direction = 1
                        x -= 1
                    elif direction == 3:
                        direction = 2
                        y += 1
                mode = 'paint'
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
            raise Exception(f'Encountered invalid opcode {opcode} at {instruction_pointer}!')

    max_x = max_y = -100000
    min_x = min_y = 100000
    for panel in painted_panels:
        x, y = map(int, panel.split(','))
        if min_x > x:
            min_x = x
        if min_y > y:
            min_y = y
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y
    for y in range(abs(min_y) + max_y + 1):
        for x in range(abs(min_x) + max_x + 1):
            print('O' if f'{min_x + x},{min_y + y}' in painted_panels else ' ', end='')
            if x + 1 == abs(min_x) + max_x + 1:
                print()


if args.part == 1:
    print(part_1())
else:
    part_2()
