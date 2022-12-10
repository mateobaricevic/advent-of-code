
with open('2019/day_1/input.txt', 'r') as input_file:
    modules = input_file.read().splitlines()
    modules = list(map(int, modules))
    # print(modules)

fuels = []
for module in modules:
    fuel = module // 3 - 2
    fuels.append(fuel)

print(sum(fuels))
