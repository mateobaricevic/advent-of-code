
file = open("input.txt")

instructions = file.read().split("\n")[:-1]

waypoint_x = 10
waypoint_y = 1
x = 0
y = 0
for i in instructions:
    if i[0] == 'F':
        x += int(i[1:]) * waypoint_x
        y += int(i[1:]) * waypoint_y
    elif i[0] == 'R':
        rotate = int(i[1:])//90
        for _ in range(rotate):
            temp = waypoint_x
            waypoint_x = waypoint_y
            waypoint_y = -temp
    elif i[0] == 'L':
        rotate = int(i[1:])//90
        for _ in range(rotate):
            temp = waypoint_x
            waypoint_x = -waypoint_y
            waypoint_y = temp
    elif i[0] == 'N':
        waypoint_y += int(i[1:])
    elif i[0] == 'S':
        waypoint_y -= int(i[1:])
    elif i[0] == 'E':
        waypoint_x += int(i[1:])
    elif i[0] == 'W':
        waypoint_x -= int(i[1:])

print(abs(x) + abs(y))
