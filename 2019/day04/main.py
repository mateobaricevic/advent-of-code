
possible = []
for i in range(245182, 790572+1):
    possible.append(str(i))

possible1 = []
for number in possible:
    if list(number) == sorted(number):
        possible1.append(number)

possible2 = []
for number in possible1:
    for digit in number:
        count = number.count(digit)
        if count >= 2:
            possible2.append(number)
            break

print(len(possible2))
