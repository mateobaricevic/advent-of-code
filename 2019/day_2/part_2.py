
with open('2019/day_2/input.txt', 'r') as input_file:
    program = input_file.read().split(',')
    program = list(map(int, program))
    # print(program)

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
                if memory[0] == 19690720:
                    print(100 * noun + verb)
                    exit()
                break
            else:
                raise Exception(f'Encountered invalid opcode {opcode} at {instruction_pointer}!')
            
            instruction_pointer += 4
