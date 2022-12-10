
file = open("input.txt", 'r')

tickets = [line.replace('\n', '') for line in file.readlines()]

seatIds = []
for ticket in tickets:
    row = int(ticket[:7].replace('B', '1').replace('F', '0'), 2)
    column = int(ticket[7:].replace('R', '1').replace('L', '0'), 2)
    seatId = row * 8 + column
    seatIds.append(seatId)

print(max(seatIds))
seatIds.sort()
a = set([x for x in range(68, 971)])
print(a ^ set(seatIds))
