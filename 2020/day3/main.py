import functools

file = open("input.txt", 'r')

geology = [list(line.replace('\n', '')) for line in file.readlines()]

height = len(geology)
width = len(geology[0])

def isTree(x, y):
    return geology[y][x%width] == '#'

def countTrees(right, down):
    x = 0
    y = 0
    count = 0
    while y < height-1:
        x += right
        y += down
        count += isTree(x, y)
    return count

counts = [countTrees(1, 1), countTrees(3, 1), countTrees(5, 1), countTrees(7, 1), countTrees(1, 2)]
print(counts)
print(functools.reduce(lambda a, b: a * b, counts))
