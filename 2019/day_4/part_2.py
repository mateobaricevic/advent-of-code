
possible = []
for i in range(245182, 790572+1):
    possible.append(str(i))

possible_1 = [number for number in possible if list(number) == sorted(number)]

possible_2 = []
for number in possible_1:
    for digit in number:
        count = number.count(digit)
        if count == 2:
            possible_2.append(number)
            break

print(len(possible_2))
