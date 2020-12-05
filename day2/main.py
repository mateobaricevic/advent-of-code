
file = open("input.txt", 'r')

correct = 0
correct2 = 0
for line in file:
    password = line.split(':')[1].replace(' ', '').replace('\n', '')
    at_least = int(line.split('-')[0])
    at_most = int(line.split(':')[0].split('-')[1].split(' ')[0])
    char = line.split(':')[0].split('-')[1].split(' ')[1]

    if at_least <= password.count(char) <= at_most:
        correct += 1

    if password[at_least-1] == char or password[at_most-1] == char:
        if password[at_least-1] == char and password[at_most-1] == char:
            continue
        else:
            correct2 += 1

print(correct)
print(correct2)
