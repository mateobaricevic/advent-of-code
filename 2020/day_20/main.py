import numpy as np
import math
import pprint
import time

file = open("input.txt")
tiles = file.read().split("\n\n")[:-1]
tiles = [t.split("\n") for t in tiles]
tiles = {int(tile[0].split(" ")[1][:-1]) : np.array([list(t) for t in tile[1:]]) for tile in tiles}
# pprint.pprint(tiles)

def matches(a, direction, b):
    match = True
    length = len(a[0])
    if direction == "up":
        for i in range(length):
            if a[0][i] != b[length-1][i]:
                match = False
                break
    elif direction == "down":
        for i in range(length):
            if a[length-1][i] != b[0][i]:
                match = False
                break
    elif direction == "left":
        for i in range(length):
            if a[i][0] != b[i][length-1]:
                match = False
                break
    elif direction == "right":
        for i in range(length):
            if a[i][length-1] != b[i][0]:
                match = False
                break
    return match

def transform(tile):
    return [tile, np.rot90(tile), np.rot90(tile, 2), np.rot90(tile, 3),
            np.flipud(tile), np.flipud(np.rot90(tile)), np.flipud(np.rot90(tile, 2)), np.flipud(np.rot90(tile, 3)),
            np.fliplr(tile), np.fliplr(np.rot90(tile)), np.fliplr(np.rot90(tile, 2)), np.fliplr(np.rot90(tile, 3))]

def neighbors(tile_id, tile):
    counts = [0 for _ in range(12)]
    results = [[None for _ in range(4)] for _ in range(12)]
    start_tiles = transform(tile)
    for i, start_tile in enumerate(start_tiles):
        result = [None for _ in range(4)]
        for t_id, t in tiles.items():
            if t_id == tile_id:
                continue
            check_tiles = transform(t)
            for check_tile in check_tiles:
                if matches(start_tile, "up", check_tile): result[0] = t_id
                if matches(start_tile, "down", check_tile): result[1] = t_id
                if matches(start_tile, "left", check_tile): result[2] = t_id
                if matches(start_tile, "right", check_tile): result[3] = t_id
        if result[0]: counts[i] += 1
        if result[1]: counts[i] += 1
        if result[2]: counts[i] += 1
        if result[3]: counts[i] += 1
        results[i] = result[:]
    for i, count in enumerate(counts):
        # print(tile_id, count, max(counts))
        # print(start_tiles[i])
        if count == max(counts):
            tiles[tile_id] = start_tiles[i]
            return results[i]
    return None

print("Getting a corner...")
start = time.time()
corner = 0
for tile_id, tile in tiles.items():
    # print(tiles[tile_id])
    if neighbors(tile_id, tile).count(None) == 2:
        corner = tile_id
        break
    # print(tiles[tile_id])
print(corner)
print("Took {:.2f} seconds.".format(time.time()-start))

image_size = int(math.sqrt(len(tiles)))
image = [[None for _ in range(image_size)] for _ in range(image_size)]
image[0][0] = corner

print("Assembling image...")
start = time.time()
for i in range(image_size):
    for j in range(image_size):
        start_tiles = transform(tiles[image[i][j]])
        start_tiles_neighbors = [neighbors(image[i][j], t) for t in start_tiles]
        # pprint.pprint(start_tiles_neighbors)
        neighbor = None
        for k, n in enumerate(start_tiles_neighbors):
            use = [False for _ in range(4)]

            if n[0] is None: use[0] = True
            if n[1] is None: use[1] = True
            if n[2] is None: use[2] = True
            if n[3] is None: use[3] = True
            if 0 <= i-1 < image_size and (image[i-1][j] == n[0] or image[i-1][j] is None): use[0] = True
            if 0 <= i+1 < image_size and (image[i+1][j] == n[1] or image[i+1][j] is None): use[1] = True
            if 0 <= j-1 < image_size and (image[i][j-1] == n[2] or image[i][j-1] is None): use[2] = True
            if 0 <= j+1 < image_size and (image[i][j+1] == n[3] or image[i][j+1] is None): use[3] = True

            if all(use):
                neighbor = n
                tiles[image[i][j]] = start_tiles[k]
                break
        # print(image[i][j], neighbor)
        if neighbor:
            if neighbor[0]: image[i-1][j] = neighbor[0]
            if neighbor[1]: image[i+1][j] = neighbor[1]
            if neighbor[2]: image[i][j-1] = neighbor[2]
            if neighbor[3]: image[i][j+1] = neighbor[3]
        else:
            print("Failed to assemble image!")
            exit()
    print("{}/{}".format(i+1, image_size))

print("Took {:.2f} seconds.".format(time.time()-start))
pprint.pprint(image, width=len(str(max(sum(image, [])))) * image_size + 2 * (image_size+1))

with open("image.txt", 'w') as file:
    for row in image:
        file.write(','.join(map(str, row)))
        file.write("\n")
print("Image saved to image.txt!")

with open("tiles.txt", 'w') as file:
    for tile_id, tile in tiles.items():
        file.write("{}\n".format(tile_id))
        for row in tile:
            file.write(''.join(row) + "\n")
        file.write("\n")
print("Tiles saved to tiles.txt!")
