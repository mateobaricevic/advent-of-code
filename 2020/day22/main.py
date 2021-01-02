
file = open("input.txt")
decks = file.read().split("\nPlayer")
decks = [list(map(int, d.split("\n")[1:-1])) for d in decks]
for d in decks:
    d.reverse()
# print(decks)

while True:
    if len(decks[0]) == 0:
        winner = decks[1]
        break
    if len(decks[1]) == 0:
        winner = decks[0]
        break
    player1 = decks[0].pop()
    player2 = decks[1].pop()
    if player1 > player2:
        decks[0].insert(0, player1)
        decks[0].insert(0, player2)
    else:
        decks[1].insert(0, player2)
        decks[1].insert(0, player1)
    # print(decks)

print(sum([w * (i+1) for i, w in enumerate(winner)]))
