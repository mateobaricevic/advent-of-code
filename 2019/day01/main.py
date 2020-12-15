
file = open("input.txt")

modules = file.read().split('\n')[:-1]

fuels = []
for module in modules:
    fuel = int(module)//3 - 2
    fuels.append(fuel)
    while fuel > 0:
        fuel = fuel//3 - 2
        if fuel > 0:
            fuels.append(fuel)

print(sum(fuels))
