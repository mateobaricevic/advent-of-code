
file = open("input.txt")

program = file.read().split('\n')[:-1]
program = [instruction.split(' = ') for instruction in program]
# print(program)

memory = {}
mask = program[0][1]
for instruction in program:
    if instruction[0] == "mask":
        mask = instruction[1]
    elif instruction[0][:3] == "mem":
        binary_value = str(bin(int(instruction[1])))[2:].zfill(36)
        memory[instruction[0][4:-1]] = "".join([char if mask[i] == 'X' else mask[i] for i, char in enumerate(binary_value)])

# print(memory)

sum = 0
for key, value in memory.items():
    sum += int(value, 2)

print(sum)

def generateAddresses(address):
    result = [""]
    for value in address:
        if value != 'X':
            result = [i + value for i in result]
        else:
            result = [i + '1' for i in result] + [i + '0' for i in result]
    return result

memory = {}
mask = program[0][1]
for instruction in program:
    if instruction[0] == "mask":
        mask = instruction[1]
    elif instruction[0][:3] == "mem":
        binary_address = str(bin(int(instruction[0][4:-1])))[2:].zfill(36)
        address = ""
        for i, char in enumerate(mask):
            if mask[i] == '0':
                address += binary_address[i]
            elif mask[i] == '1':
                address += '1'
            elif mask[i] == 'X':
                address += 'X'
        addresses = generateAddresses(address)
        for a in addresses:
            memory[a] = instruction[1]

sum = 0
for key, value in memory.items():
    sum += int(value)

print(sum)