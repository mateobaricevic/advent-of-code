
file = open("input.txt")
flips = file.read().split("\n")[:-1]
# print(flips)

tiles = {}
black_tiles = []
for flip in flips:
    flip = list(flip)
    i = j = 0
    # print("start", i, j)
    while len(flip) > 0:
        direction = flip.pop(0)
        if direction not in ["e", "w"]:
            direction += flip.pop(0)
        if direction == "e":
            j += 1
        elif direction == "se":
            if i % 2 == 0:
                i += 1
            else:
                i += 1
                j += 1
        elif direction == "sw":
            if i % 2 == 0:
                i += 1
                j -= 1
            else:
                i += 1
        elif direction == "w":
            j -= 1
        elif direction == "nw":
            if i % 2 == 0:
                i -= 1
                j -= 1
            else:
                i -= 1
        elif direction == "ne":
            if i % 2 == 0:
                i -= 1
            else:
                i -= 1
                j += 1
        # print(direction, i, j)

    if (i, j) in black_tiles:
        black_tiles.remove((i, j))
    else:
        black_tiles.append((i, j))

    if (i, j) in tiles.keys():
        tiles.pop((i, j))
    else:
        tiles[(i, j)] = 1

def neighbors(i, j):
    # e, w
    result = [(i, j-1), (i, j+1)]
    if i % 2 == 0:
        # ne, nw, se and sw
        result.append((i-1, j-1))
        result.append((i-1, j))
        result.append((i+1, j-1))
        result.append((i+1, j))
    else:
        # ne, nw, se and sw
        result.append((i-1, j))
        result.append((i-1, j+1))
        result.append((i+1, j))
        result.append((i+1, j+1))
    return result

for iteration in range(100):
    padding = set()
    for (i, j), value in tiles.items():
        if value == 1:
            ns = neighbors(i, j)
            for n in ns:
                if n not in tiles.keys():
                    padding.add(n)
    for p in padding:
        tiles[p] = 0

    change = []
    for (i, j) in tiles.keys():
        ns = neighbors(i, j)
        count = 0
        for n in ns:
            if n in black_tiles:
                count += 1
        if tiles[(i, j)] == 1:
            if count == 0 or count > 2:
                change.append((i, j))
        elif tiles[(i, j)] == 0:
            if count == 2:
                change.append((i, j))
        # if count > 0:
        #     print(i, j, count)

    for i, j in change:
        if tiles[(i, j)]:
            tiles[(i, j)] = 0
            black_tiles.remove((i, j))
        else:
            tiles[(i, j)] = 1
            black_tiles.append((i, j))

    if (iteration+1) % 10 == 0:
        print("Day {}:".format(str(iteration+1)), sum(tiles.values()))
