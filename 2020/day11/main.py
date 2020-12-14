
file = open("input.txt")

layout = file.read().split('\n')[:-1]
layout = [list(row) for row in layout]

def neighbors(list, x, y):
    result = []
    for i in range(-1, 2):
        row = x + i
        # Check if row in bounds
        if 0 <= row < len(list):
            for j in range(-1, 2):
                column = y + j
                # Check if column in bounds
                if 0 <= column < len(list[row]):
                    # Don't add element that we want neighbors of
                    if row == x and column == y:
                        continue
                    result.append(list[row][column])
    return result

layout1 = layout[:]
while True:
    new_layout = []
    for i in range(len(layout1)):
        new_row = []
        for j in range(len(layout1[i])):
            n = neighbors(layout1, i, j)
            if layout1[i][j] == 'L' and n.count('#') == 0:
                new_row.append('#')
            elif layout1[i][j] == '#' and n.count('#') >= 4:
                new_row.append('L')
            else:
                new_row.append(layout1[i][j])
        new_layout.append(new_row)
    if new_layout == layout1:
        break
    else:
        layout1 = new_layout

def neighbors2(list, x, y):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    result = []
    for dir in dirs:
        for i in range(1, len(list)):
            row = x + i * dir[0]
            column = y + i * dir[1]
            # Check if row and column in bounds
            if 0 <= row < len(list) and 0 <= column < len(list[row]):
                if list[row][column] != '.':
                    result.append(list[row][column])
                    break
    return result

layout2 = layout[:]
while True:
    new_layout = []
    for i in range(len(layout2)):
        new_row = []
        for j in range(len(layout2[i])):
            n = neighbors2(layout2, i, j)
            if layout2[i][j] == 'L' and n.count('#') == 0:
                new_row.append('#')
            elif layout2[i][j] == '#' and n.count('#') >= 5:
                new_row.append('L')
            else:
                new_row.append(layout2[i][j])
        new_layout.append(new_row)
    if new_layout == layout2:
        break
    else:
        layout2 = new_layout

count1 = count2 = 0
for row in layout1:
    count1 += row.count('#')
for row in layout2:
    count2 += row.count('#')

print(count1)
print(count2)