
file = open("input.txt")

instructions = file.read().split("\n")[:-1]

direction_y = 0
direction_x = 1
x = 0
y = 0
for i in instructions:
    if i[0] == 'F':
        x += int(i[1:]) * direction_x
        y += int(i[1:]) * direction_y
    elif i[0] == 'R':
        rotate = int(i[1:])//90
        for _ in range(rotate):
            temp = direction_x
            direction_x = direction_y
            direction_y = -temp
    elif i[0] == 'L':
        rotate = int(i[1:])//90
        for _ in range(rotate):
            temp = direction_x
            direction_x = -direction_y
            direction_y = temp
    elif i[0] == 'N':
        y += int(i[1:])
    elif i[0] == 'S':
        y -= int(i[1:])
    elif i[0] == 'E':
        x += int(i[1:])
    elif i[0] == 'W':
        x -= int(i[1:])

print(abs(x) + abs(y))
