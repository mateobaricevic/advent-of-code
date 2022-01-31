# Part 1
# commands = []
# with open("2021/day02/input.txt", "r") as file:
#   for line in file:
#     commands.append(line.replace("\n", ""))

# position = [0, 0]
# for command in commands:
#   instruction = command.split(" ")
#   if instruction[0] == "forward":
#     position[0] += int(instruction[1])
#   elif instruction[0] == "down":
#     position[1] += int(instruction[1])
#   elif instruction[0] == "up":
#     position[1] -= int(instruction[1])

# print(position[0] * position[1])

# Part 2
commands = []
with open("2021/day02/input.txt", "r") as file:
  for line in file:
    commands.append(line.replace("\n", ""))

position = [0, 0]
aim = 0
for command in commands:
  instruction = command.split(" ")
  if instruction[0] == "forward":
    position[0] += int(instruction[1])
    position[1] += aim * int(instruction[1])
  elif instruction[0] == "down":
    aim += int(instruction[1])
  elif instruction[0] == "up":
    aim -= int(instruction[1])

print(position[0] * position[1])
