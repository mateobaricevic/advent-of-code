
# measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
measurements = []
with open("2021/day01/input.txt", "r") as file:
  for line in file:
    measurements.append(int(line))

# print(measurements)

# Part 2
measurementsSum = []
for i in range(2, len(measurements)):
  measurementsSum.append(measurements[i-2] + measurements[i-1] + measurements[i])

# print(measurementsSum)

measurements = measurementsSum

count = 0
for i in range(1, len(measurements)):
  if measurements[i] - measurements[i-1] > 0:
    count += 1

print(count)
