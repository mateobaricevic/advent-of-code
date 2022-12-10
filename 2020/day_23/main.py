
cups = "193467258"
# cups = "389125467"
cups = [int(c) for c in cups]

position = 0
iteration = 0
while True:
    if position == len(cups):
        position = 0
    if iteration == 100:
        break

    length = len(cups)
    pick_up = []
    pos = position + 1
    while pos < length and len(pick_up) < 3:
        pick_up.append(cups[pos])
        pos += 1
    pos = 0
    while len(pick_up) < 3:
        pick_up.append(cups[pos])
        pos += 1

    destination = cups[position]-1
    if destination < 1:
        destination = max(cups)
    while destination in pick_up:
        destination -= 1
        if destination < 1:
            destination = max(cups)

    # print(iteration + 1)
    # print(cups[position], cups)
    # print(pick_up)
    # print(destination)
    # print('-' * 20)

    index_before = cups.index(destination)

    for cup in pick_up:
        cups.remove(cup)

    index = cups.index(destination) + 1
    for i, cup in enumerate(pick_up):
        cups.insert(index + i, cup)

    index = index_before - 3
    if index < 0: index += length
    while cups.index(destination) != index:
        cups.append(cups.pop(0))

    position += 1
    iteration += 1

print("".join([str(cup) for cup in cups[cups.index(1)+1:]]) + "".join([str(cup) for cup in cups[0:cups.index(1)]]))
