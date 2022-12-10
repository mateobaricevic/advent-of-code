
with open('2019/day_2/input.txt', 'r') as input_file:
    program = input_file.read().split(',')
    program = list(map(int, program))
    # print(program)

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
        print(memory[0])
        exit()
    else:
        raise Exception(f'Encountered invalid opcode {opcode} at {instruction_pointer}!')
    
    instruction_pointer += 4
