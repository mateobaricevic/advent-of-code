
file = open("input.txt")

notes = file.read().split("\n")[:-1]

depart = int(notes[0])
buses = [(int(bus), i) if bus != 'x' else 0 for i, bus in enumerate(notes[1].split(','))]
buses[:] = [bus for bus in buses if bus != 0]
# print(buses)

time = min([((depart//bus+1)*bus, bus) for bus, _ in buses])
print((time[0]-depart) * time[1])

t, step = 0, 1
for bus, mins in buses:
    while (t + mins) % bus != 0:
        t += step
    step *= bus

print(t)
