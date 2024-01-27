import argparse
import pathlib

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
    memory = program[:]

    instruction_pointer = 0
    while True:
        operation = str(memory[instruction_pointer])
        # print(operation)

        while len(operation) < 5:
            operation = '0' + operation

        opcode = int(operation[3:])
        parameter_1_mode = int(operation[2])
        parameter_2_mode = int(operation[1])
        parameter_3_mode = int(operation[0])
        # print(memory)

        if opcode == 1:  # Addition
            parameter_1 = memory[instruction_pointer + 1]
            parameter_2 = memory[instruction_pointer + 2]
            parameter_3 = memory[instruction_pointer + 3]

            argument_1 = parameter_1 if parameter_1_mode else memory[parameter_1]
            argument_2 = parameter_2 if parameter_2_mode else memory[parameter_2]

            memory[parameter_3] = argument_1 + argument_2

            instruction_pointer += 4
        elif opcode == 2:  # Multiplication
            parameter_1 = memory[instruction_pointer + 1]
            parameter_2 = memory[instruction_pointer + 2]
            parameter_3 = memory[instruction_pointer + 3]

            argument_1 = parameter_1 if parameter_1_mode else memory[parameter_1]
            argument_2 = parameter_2 if parameter_2_mode else memory[parameter_2]

            memory[parameter_3] = argument_1 * argument_2

            instruction_pointer += 4
        elif opcode == 3:  # Input
            parameter_1 = memory[instruction_pointer + 1]

            memory[parameter_1] = int(input('Input value: '))

            instruction_pointer += 2
        elif opcode == 4:  # Output
            parameter_1 = memory[instruction_pointer + 1]

            argument_1 = parameter_1 if parameter_1_mode else memory[parameter_1]

            print(argument_1)

            instruction_pointer += 2
        elif opcode == 99:  # Exit
            break
        else:  # Invalid opcode
            raise Exception(f'Encountered invalid opcode {opcode} at {instruction_pointer}!')


def part_2():
    memory = program[:]

    instruction_pointer = 0
    while True:
        operation = str(memory[instruction_pointer])
        # print(operation)

        while len(operation) < 5:
            operation = '0' + operation

        opcode = int(operation[3:])
        parameter_1_mode = int(operation[2])
        parameter_2_mode = int(operation[1])
        parameter_3_mode = int(operation[0])
        # print(memory)

        if opcode == 1:  # Addition
            parameter_1 = memory[instruction_pointer + 1]
            parameter_2 = memory[instruction_pointer + 2]
            parameter_3 = memory[instruction_pointer + 3]

            argument_1 = parameter_1 if parameter_1_mode else memory[parameter_1]
            argument_2 = parameter_2 if parameter_2_mode else memory[parameter_2]

            memory[parameter_3] = argument_1 + argument_2

            instruction_pointer += 4
        elif opcode == 2:  # Multiplication
            parameter_1 = memory[instruction_pointer + 1]
            parameter_2 = memory[instruction_pointer + 2]
            parameter_3 = memory[instruction_pointer + 3]

            argument_1 = parameter_1 if parameter_1_mode else memory[parameter_1]
            argument_2 = parameter_2 if parameter_2_mode else memory[parameter_2]

            memory[parameter_3] = argument_1 * argument_2

            instruction_pointer += 4
        elif opcode == 3:  # Input
            parameter_1 = memory[instruction_pointer + 1]

            memory[parameter_1] = int(input('Input value: '))

            instruction_pointer += 2
        elif opcode == 4:  # Output
            parameter_1 = memory[instruction_pointer + 1]

            argument_1 = parameter_1 if parameter_1_mode else memory[parameter_1]

            print(argument_1)

            instruction_pointer += 2
        elif opcode == 5:  # Jump if true
            parameter_1 = memory[instruction_pointer + 1]
            parameter_2 = memory[instruction_pointer + 2]

            argument_1 = parameter_1 if parameter_1_mode else memory[parameter_1]
            argument_2 = parameter_2 if parameter_2_mode else memory[parameter_2]

            if argument_1 != 0:
                instruction_pointer = argument_2
            else:
                instruction_pointer += 3
        elif opcode == 6:  # Jump if false
            parameter_1 = memory[instruction_pointer + 1]
            parameter_2 = memory[instruction_pointer + 2]

            argument_1 = parameter_1 if parameter_1_mode else memory[parameter_1]
            argument_2 = parameter_2 if parameter_2_mode else memory[parameter_2]

            if argument_1 == 0:
                instruction_pointer = argument_2
            else:
                instruction_pointer += 3
        elif opcode == 7:  # Less than
            parameter_1 = memory[instruction_pointer + 1]
            parameter_2 = memory[instruction_pointer + 2]
            parameter_3 = memory[instruction_pointer + 3]

            argument_1 = parameter_1 if parameter_1_mode else memory[parameter_1]
            argument_2 = parameter_2 if parameter_2_mode else memory[parameter_2]

            if argument_1 < argument_2:
                memory[parameter_3] = 1
            else:
                memory[parameter_3] = 0

            instruction_pointer += 4
        elif opcode == 8:  # Equals
            parameter_1 = memory[instruction_pointer + 1]
            parameter_2 = memory[instruction_pointer + 2]
            parameter_3 = memory[instruction_pointer + 3]

            argument_1 = parameter_1 if parameter_1_mode else memory[parameter_1]
            argument_2 = parameter_2 if parameter_2_mode else memory[parameter_2]

            if argument_1 == argument_2:
                memory[parameter_3] = 1
            else:
                memory[parameter_3] = 0

            instruction_pointer += 4
        elif opcode == 99:  # Exit
            break
        else:  # Invalid opcode
            raise Exception(f'Encountered invalid opcode {opcode} at {instruction_pointer}!')


if args.part == 1:
    part_1()
else:
    part_2()
