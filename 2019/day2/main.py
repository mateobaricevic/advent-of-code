import pprint

file = open("input.txt")

original_program = file.read().replace('\n', '').split(',')
original_program = [int(i) for i in original_program]
# pprint.pprint(program)

for i in range(0, 100):
    for j in range(0, 100):
        noun = i
        verb = j

        program = original_program[:]
        program[1] = noun
        program[2] = verb

        instructionPointer = 0
        while True:
            opcode = program[instructionPointer]
            position1 = program[instructionPointer+1]
            position2 = program[instructionPointer+2]
            output = program[instructionPointer+3]

            if opcode == 1:
                program[output] = program[position1] + program[position2]
            elif opcode == 2:
                program[output] = program[position1] * program[position2]
            elif opcode == 99:
                break

            instructionPointer += 4

        if program[0] == 19690720:
            print(100 * noun + verb)