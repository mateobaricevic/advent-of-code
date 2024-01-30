import argparse
import os
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


def print_screen(screen):
    os.system('clear')
    for y in range(22):
        for x in range(38):
            print(screen[f'{x},{y}'], end='')
            if x + 1 == 38:
                print()


def part_1():
    memory = defaultdict(int)
    for address, value in enumerate(program):
        memory[address] = value

    instruction_pointer = 0
    relative_base = 0
    x, y = 0, 0
    screen = {}
    mode = 'x'
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
            memory[parameter_1] = int(input('Input: '))
            instruction_pointer += 2
        elif opcode == 4:  # Output
            if mode == 'x':
                x = argument_1
                mode = 'y'
            elif mode == 'y':
                y = argument_1
                mode = 'place'
            elif mode == 'place':
                if argument_1 == 0:  # Empty
                    screen[f'{x},{y}'] = ' '
                elif argument_1 == 1:  # Wall
                    screen[f'{x},{y}'] = 'X'
                elif argument_1 == 2:  # Block
                    screen[f'{x},{y}'] = '='
                elif argument_1 == 3:  # Horizontal Paddle
                    screen[f'{x},{y}'] = '-'
                elif argument_1 == 4:  # Ball
                    screen[f'{x},{y}'] = 'O'
                mode = 'x'
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

    print_screen(screen)

    return sum([1 for value in screen.values() if value == '='])


def part_2():
    memory = defaultdict(int)
    for address, value in enumerate(program):
        memory[address] = value
    memory[0] = 2

    instruction_pointer = 0
    relative_base = 0
    x, y = 0, 0
    ball_x, paddle_x = 0, 0
    screen = {}
    mode = 'x'
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
            print_screen(screen)

            # Manual input
            # key_press = ''
            # while key_press not in ['left', 'down', 'right']:
            #     time.sleep(0.1)
            #     key_press = keyboard.read_key()
            # if key_press == 'left':
            #     memory[parameter_1] = -1
            # elif key_press == 'down':
            #     memory[parameter_1] = 0
            # elif key_press == 'right':
            #     memory[parameter_1] = 1

            # Automatic input
            if paddle_x > ball_x:
                memory[parameter_1] = -1
            elif paddle_x < ball_x:
                memory[parameter_1] = 1
            else:
                memory[parameter_1] = 0

            instruction_pointer += 2
        elif opcode == 4:  # Output
            if mode == 'x':
                x = argument_1
                mode = 'y'
            elif mode == 'y':
                y = argument_1
                mode = 'place'
            elif mode == 'place':
                if x == -1 and y == 0:
                    print(f'\nScore: {argument_1}')
                elif argument_1 == 0:  # Empty
                    screen[f'{x},{y}'] = ' '
                elif argument_1 == 1:  # Wall
                    screen[f'{x},{y}'] = 'X'
                elif argument_1 == 2:  # Block
                    screen[f'{x},{y}'] = '='
                elif argument_1 == 3:  # Horizontal Paddle
                    paddle_x = x
                    screen[f'{x},{y}'] = '-'
                elif argument_1 == 4:  # Ball
                    ball_x = x
                    screen[f'{x},{y}'] = 'O'
                mode = 'x'
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


if args.part == 1:
    print(part_1())
else:
    part_2()
