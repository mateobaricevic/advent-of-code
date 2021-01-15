
file = open("input.txt")
flips = file.read().split("\n")[:-1]
# print(flips)

length = max(list(map(len, flips))) * 2
tiles = []
for flip in flips:
    flip = list(flip)
    i = j = length // 2
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
    if (i, j) in tiles:
        tiles.remove((i, j))
    else:
        tiles.append((i, j))

print(len(tiles))
