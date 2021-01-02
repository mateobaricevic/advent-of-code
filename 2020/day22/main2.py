
file = open("input.txt")
decks = file.read().split("\nPlayer")
decks = [list(map(int, d.split("\n")[1:-1])) for d in decks]
for d in decks:
    d.reverse()
# print(decks)

winner_deck = []
def game(deck1, deck2):
    global winner_deck
    # deck1.reverse()
    # deck2.reverse()
    # print(deck1)
    # print(deck2)
    # deck1.reverse()
    # deck2.reverse()

    played = []
    while True:
        if len(deck1) == 0:
            winner_deck = deck2
            return 2
        if len(deck2) == 0:
            winner_deck = deck1
            return 1
        check = (deck1[:], deck2[:])
        if check in played:
            winner_deck = deck1
            return 1
        played.append(check)
        player1 = deck1.pop()
        player2 = deck2.pop()
        recursive_winner = 0
        if len(deck1) >= player1 and len(deck2) >= player2:
            recursive_winner = game(deck1[len(deck1)-player1:], deck2[len(deck2)-player2:])
        if recursive_winner == 1:
            deck1.insert(0, player1)
            deck1.insert(0, player2)
        elif recursive_winner == 2:
            deck2.insert(0, player2)
            deck2.insert(0, player1)
        else:
            if player1 > player2:
                deck1.insert(0, player1)
                deck1.insert(0, player2)
            else:
                deck2.insert(0, player2)
                deck2.insert(0, player1)
        # deck1.reverse()
        # deck2.reverse()
        # print(deck1)
        # print(deck2)
        # deck1.reverse()
        # deck2.reverse()

game(decks[0][:], decks[1][:])
print(sum([w * (i+1) for i, w in enumerate(winner_deck)]))
