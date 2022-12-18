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

vaporized = [(station_x, station_y)]
while len(vaporized) != len(asteroids):
    closest_points = {}
    for x, y in asteroids:
        if (x, y) not in vaporized:
            dx, dy = x - station_x, y - station_y
            dx, dy = dx // math.gcd(dx, dy), dy // math.gcd(dx, dy)
            closest_x, closest_y = closest_points.get((dx, dy), (float('inf'), float('inf')))
            if abs(x - station_x) + abs(y - station_y) < abs(closest_x - station_x) + abs(closest_y - station_y):
                closest_points[(dx, dy)] = (x, y)
    vaporized += sorted(closest_points.values(), key=lambda p:-math.atan2(p[0] - station_x, p[1] - station_y))

print(vaporized[200][0] * 100 + vaporized[200][1])
