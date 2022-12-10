
file = open("input.txt")

notes = file.read()[:-2].split("\n\n")
# notes = "class: 1-3 or 5-7\nrow: 6-11 or 33-44\nseat: 13-40 or 45-50\n\nyour ticket:\n7,1,14\n\nnearby tickets:\n7,3,47\n40,4,50\n55,2,20\n38,6,12\n\n".split("\n\n")
# notes = "class: 0-1 or 4-19\nrow: 0-5 or 8-19\nseat: 0-13 or 16-19\n\nyour ticket:\n11,12,13\n\nnearby tickets:\n3,9,18\n15,1,5\n5,14,9\n\n".split("\n\n")
notes = [n.split("\n") for n in notes]
# print(notes)

rules = [rule.split(": ") for rule in notes[0]]
rules = [[rule[0]] + [[int(value) for value in r.split("-")] for r in rule[1].split(" or ")] for rule in rules]
# print(rules)

my_ticket = [int(value) for value in notes[1][1:][0].split(",")]
# print(my_ticket)

tickets = [[int(value) for value in ticket.split(",")] for ticket in notes[2][1:]]
# print(tickets)

valid_tickets = tickets[:]
valueSum = 0
for t in tickets:
    values_valid = []
    for value in t:
        rules_valid = []
        for rule in rules:
            valid = False
            for r in rule[1:]:
                if r[0] <= value <= r[1]:
                    valid = True
            rules_valid.append(valid)
        values_valid.append(any(rules_valid))
        if not any(rules_valid):
            valueSum += value
    if not all(values_valid):
        valid_tickets.remove(t)

print(valueSum)

valid_tickets.append(my_ticket)
# Transpose
positions_tickets = list(map(list, zip(*valid_tickets)))

def isListInRange(list, a, b, c, d):
    result = []
    for value in list:
        result.append(a <= value <= b or c <= value <= d)
    return all(result)

positions = []
departure_indexes = []
for i, rule in enumerate(rules):
    if "departure" in rule[0]:
        departure_indexes.append(i)
    valid_indexes = []
    for j, position in enumerate(positions_tickets):
        if isListInRange(position, rule[1][0], rule[1][1], rule[2][0], rule[2][1]):
            valid_indexes.append(j)
    positions.append(valid_indexes)

for _ in range(len(positions)):
    for i, pos in enumerate(positions):
        if type(pos) == list:
            if len(pos) == 1:
                positions[i] = pos[0]
                for p in positions:
                    if type(p) == list:
                        p.remove(pos[0])
# print(positions)

product = 1
for i in departure_indexes:
    product *= my_ticket[positions[i]]

print(product)
