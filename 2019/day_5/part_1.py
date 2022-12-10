
with open('2019/day_5/input.txt', 'r') as input_file:
    program = input_file.read().split(',')
    program = list(map(int, program))
    # print(program)

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
    
    if opcode == 1: # Addition
        parameter_1 = memory[instruction_pointer + 1]
        parameter_2 = memory[instruction_pointer + 2]
        parameter_3 = memory[instruction_pointer + 3]
        
        argument_1 = parameter_1 if parameter_1_mode else memory[parameter_1]
        argument_2 = parameter_2 if parameter_2_mode else memory[parameter_2]
        
        memory[parameter_3] = argument_1 + argument_2
        
        instruction_pointer += 4
        
    elif opcode == 2: # Multiplication
        parameter_1 = memory[instruction_pointer + 1]
        parameter_2 = memory[instruction_pointer + 2]
        parameter_3 = memory[instruction_pointer + 3]
        
        argument_1 = parameter_1 if parameter_1_mode else memory[parameter_1]
        argument_2 = parameter_2 if parameter_2_mode else memory[parameter_2]
        
        memory[parameter_3] = argument_1 * argument_2
        
        instruction_pointer += 4
        
    elif opcode == 3: # Input
        parameter_1 = memory[instruction_pointer + 1]
        
        memory[parameter_1] = int(input('Input value: '))
        
        instruction_pointer += 2

    elif opcode == 4: # Output
        parameter_1 = memory[instruction_pointer + 1]
        
        argument_1 = parameter_1 if parameter_1_mode else memory[parameter_1]
        
        print(argument_1)
        
        instruction_pointer += 2
        
    elif opcode == 99: # Exit
        exit()
        
    else: # Invalid opcode
        raise Exception(f'Encountered invalid opcode {opcode} at {instruction_pointer}!')
