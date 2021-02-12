
file = open("input.txt")

program = file.read().replace('\n', '').split(',')
program = [int(i) for i in program]

instruction = 0
while True:
    operation = str(program[instruction])

    while len(operation) < 5:
        operation = '0' + operation
    opcode = int(operation[3:])
    mode1 = int(operation[2])
    mode2 = int(operation[1])
    mode3 = int(operation[0])

    if opcode == 1:
        parameter1 = program[instruction+1]
        parameter2 = program[instruction+2]
        parameter3 = program[instruction+3]

        program[parameter3] = (parameter1 if mode1 else program[parameter1]) + (parameter2 if mode2 else program[parameter2])
        instruction += 4
    elif opcode == 2:
        parameter1 = program[instruction+1]
        parameter2 = program[instruction+2]
        parameter3 = program[instruction+3]

        program[parameter3] = (parameter1 if mode1 else program[parameter1]) * (parameter2 if mode2 else program[parameter2])
        instruction += 4
    elif opcode == 3:
        parameter1 = program[instruction+1]

        program[parameter1] = int(input("Input: "))
        instruction += 2
    elif opcode == 4:
        parameter1 = program[instruction+1]

        print(parameter1 if mode1 else program[parameter1])
        instruction += 2
    elif opcode == 5:
        parameter1 = program[instruction+1]
        parameter2 = program[instruction+2]

        if (parameter1 if mode1 else program[parameter1]):
            instruction = (parameter2 if mode2 else program[parameter2])
        else:
            instruction += 3
    elif opcode == 6:
        parameter1 = program[instruction+1]
        parameter2 = program[instruction+2]

        if not (parameter1 if mode1 else program[parameter1]):
            instruction = (parameter2 if mode2 else program[parameter2])
        else:
            instruction += 3
    elif opcode == 7:
        parameter1 = program[instruction+1]
        parameter2 = program[instruction+2]
        parameter3 = program[instruction+3]

        if (parameter1 if mode1 else program[parameter1]) < (parameter2 if mode2 else program[parameter2]):
            program[parameter3] = 1
        else:
            program[parameter3] = 0
        instruction += 4
    elif opcode == 8:
        parameter1 = program[instruction+1]
        parameter2 = program[instruction+2]
        parameter3 = program[instruction+3]

        if (parameter1 if mode1 else program[parameter1]) == (parameter2 if mode2 else program[parameter2]):
            program[parameter3] = 1
        else:
            program[parameter3] = 0
        instruction += 4
    elif opcode == 99:
        break
