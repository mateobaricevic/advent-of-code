import math

with open('2019/day_10/input.txt', 'r') as input_file:
    asteroid_map = input_file.read().split()
    # print(asteroid_map)

asteroids = []
for y, row in enumerate(asteroid_map):
    for x, column in enumerate(row):
        if column == '#':
            asteroids.append((x, y))
# print(asteroids)

max_visible = 0
station_x = station_y = 0
for x, y in asteroids:
    points = set()
    for x2, y2 in asteroids:
        if (x, y) != (x2, y2):
            dx, dy = x - x2, y - y2
            dx, dy = dx // math.gcd(dx, dy), dy // math.gcd(dx, dy)
            points.add((dx, dy))
    if len(points) > max_visible:
        max_visible = len(points)
        station_x, station_y = x, y

print(max_visible)
