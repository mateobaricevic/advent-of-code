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
    memory[1] = 12
    memory[2] = 2

    instruction_pointer = 0
    while True:
        opcode = memory[instruction_pointer]
        # print(memory)

        if opcode == 1:
            parameter_1 = memory[instruction_pointer + 1]
            parameter_2 = memory[instruction_pointer + 2]
            parameter_3 = memory[instruction_pointer + 3]
            memory[parameter_3] = memory[parameter_1] + memory[parameter_2]
        elif opcode == 2:
            parameter_1 = memory[instruction_pointer + 1]
            parameter_2 = memory[instruction_pointer + 2]
            parameter_3 = memory[instruction_pointer + 3]
            memory[parameter_3] = memory[parameter_1] * memory[parameter_2]
        elif opcode == 99:
            break
        else:
            raise Exception(f'Encountered invalid opcode {opcode} at {instruction_pointer}!')

        instruction_pointer += 4

    return memory[0]


def part_2():
    for noun in range(0, 100):
        for verb in range(0, 100):
            memory = program[:]
            memory[1] = noun
            memory[2] = verb

            instruction_pointer = 0
            while True:
                opcode = memory[instruction_pointer]
                # print(memory)

                if opcode == 1:
                    parameter_1 = memory[instruction_pointer + 1]
                    parameter_2 = memory[instruction_pointer + 2]
                    parameter_3 = memory[instruction_pointer + 3]
                    memory[parameter_3] = memory[parameter_1] + memory[parameter_2]
                elif opcode == 2:
                    parameter_1 = memory[instruction_pointer + 1]
                    parameter_2 = memory[instruction_pointer + 2]
                    parameter_3 = memory[instruction_pointer + 3]
                    memory[parameter_3] = memory[parameter_1] * memory[parameter_2]
                elif opcode == 99:
                    break
                else:
                    raise Exception(f'Encountered invalid opcode {opcode} at {instruction_pointer}!')

                instruction_pointer += 4

            if memory[0] == 19690720:
                return 100 * noun + verb


if args.part == 1:
    print(part_1())
else:
    print(part_2())
