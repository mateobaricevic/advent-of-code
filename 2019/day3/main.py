
file = open("input.txt")

lines = file.read().split("\n")
# lines = ["R8,U5,L5,D3", "U7,R6,D4,L4"] # 30
# lines = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"] # 610
# lines = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"] # 410

def get_grid(line):
    # coords: steps
    grid = {}

    x = 0
    y = 0
    step = 0

    for move in line:
        direction = move[0]
        distance = int(move[1:])

        dir_x = dir_y = 0
        if direction == 'U':
            dir_y = -1
        if direction == 'D':
            dir_y = 1
        if direction == 'L':
            dir_x = -1
        if direction == 'R':
            dir_x = 1

        for _ in range(distance):
            x += dir_x
            y += dir_y

            step += 1

            if (x, y) not in grid:
                grid[(x, y)] = step

    return grid

line1 = get_grid(lines[0].split(','))
line2 = get_grid(lines[1].split(','))

intersections = list(set(line1.keys()) & set(line2.keys()))

def get_shortest():
    distances = []
    for intersection in intersections:
        dist = abs(intersection[0]) + abs(intersection[1])
        distances.append(dist)
    return min(distances)

print(get_shortest())

def get_fewest():
    combined_steps = [line1[i] + line2[i] for i in intersections]
    return min(combined_steps)

print(get_fewest())
