import numpy as np
import pprint
import functools

def transform(tile):
    return [tile, np.rot90(tile), np.rot90(tile, 2), np.rot90(tile, 3),
            np.flipud(tile), np.flipud(np.rot90(tile)), np.flipud(np.rot90(tile, 2)), np.flipud(np.rot90(tile, 3)),
            np.fliplr(tile), np.fliplr(np.rot90(tile)), np.fliplr(np.rot90(tile, 2)), np.fliplr(np.rot90(tile, 3))]

file = open("tiles.txt")
tiles = file.read().split("\n\n")[:-1]
tiles = [t.split("\n") for t in tiles]
tiles = {int(tile[0]) : [t for t in tile[1:]] for tile in tiles}
# print(tiles)

file = open("image.txt")
image_ids = [list(map(int, line.split(","))) for line in file.read().split("\n")[:-1]]
# pprint.pprint(image_ids)

print(image_ids[0][0] * image_ids[0][len(image_ids) - 1] * image_ids[len(image_ids) - 1][0] * image_ids[len(image_ids) - 1][len(image_ids) - 1])

# Remove borders
for tile_id, tile in tiles.items():
    without_borders = []
    for row in tile[1:-1]:
        without_borders.append(row[1:-1])
    tiles[tile_id] = without_borders

image_tiles = [[tiles[image_ids[i][j]] for j in range(len(image_ids[i]))] for i in range(len(image_ids))]
image_tiles = [[image_tiles[i][j] for j in range(len(image_tiles[i]))] for i in range(len(image_tiles))]
# pprint.pprint(image_tiles, width=50)

image = [['' for _ in range(len(image_tiles[0][0]))] for _ in range(len(image_tiles[0]))]
for i in range(len(image_tiles)):
    for row in range(len(image_tiles[i][0])):
        for j in range(len(image_tiles[i])):
            image[i][row] += image_tiles[i][j][row]
image = functools.reduce(lambda a, b: a + b, image)
# pprint.pprint(image)

sea_monster = ["                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   "]

def markSeaMonster(i, x, y):
    global images

    for row in range(len(sea_monster)):
        for column in range(len(sea_monster[row])):
            if sea_monster[row][column] == "#":
                images[i][x+row][y+column] = "O"

image = [list(r) for r in image]
images = transform(image)
counts = [0 for _ in range(len(images))]
for index in range(len(images)):
    for i in range(len(image)-len(sea_monster)):
        for j in range(len(image[i])-len(sea_monster[0])):
            rows = []
            for row in range(len(sea_monster)):
                row_check = True
                for column in range(len(sea_monster[row])):
                    if sea_monster[row][column] == "#":
                        if images[index][i+row][j+column] != "#":
                            row_check = False
                            break
                rows.append(row_check)
                if not row_check:
                    break
            if all(rows):
                markSeaMonster(index, i, j)
                counts[index] += 1

for i in range(len(counts)):
    if counts[i] == max(counts):
        image = [list(row) for row in list(images[i])]
        image = ["".join(row) for row in image]
        # pprint.pprint(image)
        print(sum([row.count("#") for row in image]))
        break
