
file = open("input.txt")

z0 = file.read().split("\n")[:-1]
# z0 = ['.#.', '..#', '###']
space = {0: z0}
hyperspace = {0: {0: z0}}

def neighbors3d(space, z, y, x):
    result = []
    for i in range(-1, 2):
        new_z = z + i
        # Check if z in bounds
        if min(space.keys()) <= new_z < max(space.keys())+1:
            for j in range(-1, 2):
                new_y = y + j
                # Check if y in bounds
                if 0 <= new_y < len(space[new_z]):
                    for k in range(-1, 2):
                        new_x = x + k
                        # Check if x in bounds
                        if 0 <= new_x < len(space[new_z][new_y]):
                            # Don't add element that we want neighbors of
                            if new_z == z and new_y == y and new_x == x:
                                continue
                            result.append(space[new_z][new_y][new_x])
    return result

def neighbors4d(hyperspace, w, z, y, x):
    result = []
    for i in range(-1, 2):
        new_w = w + i
        # Check if w in bounds
        if min(hyperspace.keys()) <= new_w < max(hyperspace.keys())+1:
            for j in range(-1, 2):
                new_z = z + j
                # Check if z in bounds
                if min(hyperspace[new_w].keys()) <= new_z < max(hyperspace[new_w].keys())+1:
                    for k in range(-1, 2):
                        new_y = y + k
                        # Check if y in bounds
                        if 0 <= new_y < len(hyperspace[new_w][new_z]):
                            for l in range(-1, 2):
                                new_x = x + l
                                # Check if x in bounds
                                if 0 <= new_x < len(hyperspace[new_w][new_z][new_y]):
                                    # Don't add element that we want neighbors of
                                    if new_w == w and new_z == z and new_y == y and new_x == x:
                                        continue
                                    result.append(hyperspace[new_w][new_z][new_y][new_x])
    return result

def addSpace3d(space):
    new_space = {}
    for i in range(min(space.keys()) - 1, max(space.keys()) + 2):
        new_list = []
        if i in space.keys():
            for j in range(-1, len(space[i]) + 1):
                if 0 <= j < len(space[i]):
                    new_row = ""
                    for k in range(-1, len(space[i][j]) + 1):
                        if 0 <= k < len(space[i][j]):
                            new_row += space[i][j][k]
                        else:
                            new_row += '.'
                    new_list.append(new_row)
                else:
                    new_list.append('.' * (len(space[i]) + 2))
            new_space[i] = new_list
        else:
            string = '.' * (len(space[0]) + 2)
            new_space[i] = [string for _ in range(len(string))]
    return new_space

def addSpace4d(hyperspace):
    new_hyperspace = {}
    for i in range(min(hyperspace.keys()) - 1, max(hyperspace.keys()) + 2):
        new_space = {}
        if i in hyperspace.keys():
            for j in range(min(hyperspace[i].keys()) - 1, max(hyperspace[i].keys()) + 2):
                new_list = []
                if j in hyperspace[i].keys():
                    for k in range(-1, len(hyperspace[i][j]) + 1):
                        if 0 <= k < len(hyperspace[i][j]):
                            new_row = ""
                            for l in range(-1, len(hyperspace[i][j][k]) + 1):
                                if 0 <= l < len(hyperspace[i][j][k]):
                                    new_row += hyperspace[i][j][k][l]
                                else:
                                    new_row += '.'
                            new_list.append(new_row)
                        else:
                            new_list.append('.' * (len(hyperspace[i][j]) + 2))
                    new_space[j] = new_list
                else:
                    string = '.' * (len(hyperspace[i][0]) + 2)
                    new_space[j] = [string for _ in range(len(string))]
            new_hyperspace[i] = new_space
        else:
            for m in range(min(hyperspace[0].keys()) - 1, max(hyperspace[0].keys()) + 2):
                string = '.' * (len(hyperspace[0][0]) + 2)
                new_space[m] = [string for _ in range(len(string))]
            new_hyperspace[i] = new_space
    return new_hyperspace

for _ in range(6):
    space = addSpace3d(space)
    new_space = {}
    for j in space.keys():
        new_list = []
        for k in range(len(space[j])):
            new_row = ""
            for l in range(len(space[j][k])):
                n = neighbors3d(space, j, k, l)
                if space[j][k][l] == '#' and 2 <= n.count('#') <= 3:
                    new_row += '#'
                elif space[j][k][l] == '#':
                    new_row += '.'
                elif space[j][k][l] == '.' and n.count('#') == 3:
                    new_row += '#'
                else:
                    new_row += space[j][k][l]
            new_list.append(new_row)
        new_space[j] = new_list
    space = new_space

for _ in range(6):
    hyperspace = addSpace4d(hyperspace)
    new_hyperspace = {}
    for i in hyperspace.keys():
        new_space = {}
        for j in hyperspace[i].keys():
            new_list = []
            for k in range(len(hyperspace[i][j])):
                new_row = ""
                for l in range(len(hyperspace[i][j][k])):
                    n = neighbors4d(hyperspace, i, j, k, l)
                    if hyperspace[i][j][k][l] == '#' and 2 <= n.count('#') <= 3:
                        new_row += '#'
                    elif hyperspace[i][j][k][l] == '#':
                        new_row += '.'
                    elif hyperspace[i][j][k][l] == '.' and n.count('#') == 3:
                        new_row += '#'
                    else:
                        new_row += hyperspace[i][j][k][l]
                new_list.append(new_row)
            new_space[j] = new_list
        new_hyperspace[i] = new_space
    hyperspace = new_hyperspace

count = 0
for key, value in space.items():
    # print("z={}".format(key))
    for s in value:
        # print(s)
        count += s.count('#')
    # print()

print(count)


count = 0
for w in hyperspace.keys():
    for z, value in hyperspace[w].items():
        # print("z={}, w={}".format(z, w))
        for s in value:
            # print(s)
            count += s.count('#')
        # print()

print(count)

