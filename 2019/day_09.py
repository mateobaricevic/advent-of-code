import argparse
import pathlib
from collections import defaultdict

path = pathlib.Path(__file__)
input_file = f'{path.parent}/inputs/{path.stem}.txt'

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default=input_file)
args = parser.parse_args()

with open(args.input) as input_file:
    program = input_file.read().split(',')
    program = list(map(int, program))
    # print(program)


memory = defaultdict(int)
for address, value in enumerate(program):
    memory[address] = value

instruction_pointer = 0
relative_base = 0
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
        memory[parameter_1] = int(input('Input value: '))
        instruction_pointer += 2
    elif opcode == 4:  # Output
        print(argument_1)
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
