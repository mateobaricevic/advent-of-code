
with open('2021/day05/input.txt') as file:
  lines = [line.split(' -> ') for line in file.read().splitlines()]
  # print(lines)

start_points = []
end_points = []
for line in lines:
  start_points.append([int(number) for number in line[0].split(',')])
  end_points.append([int(number) for number in line[1].split(',')])

xs = [point[0] for point in start_points + end_points]
ys = [point[1] for point in start_points + end_points]
diagram = [['.' for _ in range(max(xs) + 1)] for _ in range(max(ys) + 1)]

def print_diagram():
  for row in diagram:
    for column in row:
      print(column, end='')
    print()

def increment(point):
  if diagram[point[1]][point[0]] == '.':
    diagram[point[1]][point[0]] = 1
  else:
    diagram[point[1]][point[0]] += 1

while len(start_points) > 0:
  start = start_points.pop()
  end = end_points.pop()
  
  # Part 1
  if start[0] == end[0]: # Horizontal
    increment(end)
    while start[1] < end[1]: # Down 0,0 -> 0,3
      increment(start)
      start[1] += 1
    while start[1] > end[1]: # Up 0,3 -> 0,0
      increment(start)
      start[1] -= 1
  
  elif start[1] == end[1]: # Vertical
    increment(end)
    while start[0] < end[0]: # Down 0,0 -> 3,0
      increment(start)
      start[0] += 1
    while start[0] > end[0]: # Up 3,0 -> 0,0
      increment(start)
      start[0] -= 1
  
  # Part 2
  elif start[0] < end[0] and start[1] < end[1]: # Diagonal \ Down 0,0 -> 3,3
    increment(end)
    while start[0] < end[0]:
      increment(start)
      start[0] += 1
      start[1] += 1
  
  elif start[0] > end[0] and start[1] > end[1]: # Diagonal \ Up 3,3 -> 0,0
    increment(end)
    while start[0] > end[0]:
      increment(start)
      start[0] -= 1
      start[1] -= 1
  
  elif start[0] < end[0] and start[1] > end[1]: # Diagonal / Down 0,3 -> 3,0
    increment(end)
    while start[0] < end[0]:
      increment(start)
      start[0] += 1
      start[1] -= 1
  
  elif start[0] > end[0] and start[1] < end[1]: # Diagonal / Up 3,0 -> 0,3
    increment(end)
    while start[0] > end[0]:
      increment(start)
      start[0] -= 1
      start[1] += 1

# print_diagram()

count = 0
for row in diagram:
  for column in row:
    if isinstance(column, int):
      if column >= 2:
        count += 1

print(f'There are {count} point(s) where at least two lines overlap.')
