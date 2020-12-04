import numpy as np

input = np.genfromtxt("input.txt", dtype=np.int)

numbers2 = []
for i in range(0, len(input)):
    for j in range(i+1, len(input)):
        if input[i] + input[j] == 2020:
            numbers2.append([input[i], input[j]])

print(numbers2)
print(numbers2[0][0]*numbers2[0][1])

numbers3 = []
for i in range(0, len(input)):
    for j in range(i+1, len(input)):
        for k in range(j+1, len(input)):
            if input[i] + input[j] + input[k] == 2020:
                numbers3.append([input[i], input[j], input[k]])

print(numbers3)
print(numbers3[0][0]*numbers3[0][1]*numbers3[0][2])