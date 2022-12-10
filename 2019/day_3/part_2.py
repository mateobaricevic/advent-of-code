
with open('2019/day_3/input.txt', 'r') as input_file:
    wires = input_file.read().splitlines()
    # print(wires)

def get_grid(wire):
    grid = {}
    x = y = step = 0

    for move in wire.split(','):
        direction = move[0]
        distance = int(move[1:])

        direction_x = direction_y = 0
        if direction == 'U':
            direction_y = -1
        if direction == 'D':
            direction_y = 1
        if direction == 'L':
            direction_x = -1
        if direction == 'R':
            direction_x = 1

        for _ in range(distance):
            x += direction_x
            y += direction_y
            step += 1
            
            if (x, y) not in grid:
                grid[(x, y)] = step

    return grid

wire_1 = get_grid(wires[0])
wire_2 = get_grid(wires[1])

intersections = list(set(wire_1.keys()) & set(wire_2.keys()))

combined_steps = [wire_1[intersection] + wire_2[intersection] for intersection in intersections]

print(min(combined_steps))
