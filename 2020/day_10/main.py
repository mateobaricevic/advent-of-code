from collections import defaultdict

file = open("input.txt")

adapters = file.read().split('\n')[:-1]
adapters = [int(a) for a in adapters]
adapters.append(0)
adapters.append(max(adapters)+3)
adapters.sort()

jolts = []
for i in range(len(adapters)-1):
    jolts.append(adapters[i+1] - adapters[i])

print(jolts.count(1) * jolts.count(3))

paths = defaultdict(int)
paths[0] = 1
for adapter in adapters:
    for diff in range(1, 4):
        next_adapter = adapter + diff
        if next_adapter in adapters:
            paths[next_adapter] += paths[adapter]
print(paths[max(adapters)])
