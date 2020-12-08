import pprint

file = open("input.txt", 'r')

original_program = file.read().split('\n')[:-1]
# pprint.pprint(original_program)

changed = 0
fixed = False
while not fixed:
    program = original_program[:]
    program[changed] = program[changed].replace("jmp", "nop")

    line = 0
    accumulator = 0
    ran = []
    while True:
        if line in ran:
            break

        if line == len(program):
            print("Program fixed.")
            print("Line changed:", changed)
            print("Output:", accumulator)
            fixed = True
            break

        ran.append(line)
        operation = program[line].split(' ')[0]
        argument = int(program[line].split(' ')[1])

        if operation == "acc":
            accumulator += argument
        elif operation == "jmp":
            line += argument
            continue

        line += 1

    changed += 1
