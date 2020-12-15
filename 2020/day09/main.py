
file = open("input.txt")

data = file.read().split('\n')[:-1]
data = [int(i) for i in data]
#print(data)

preambleLength = 25
for i in range(preambleLength, len(data)):
    numbers = [data[d] for d in range(0, preambleLength)]

    valid = False
    for j in range(0, len(numbers)):
        for k in range(0, len(numbers)):
            if data[i-1-j] + data[i-1-k] == data[i]:
                valid = True
                break
        if valid:
            break

    if not valid:
        number = data[i]
        print(number)
        for length in range(2, len(data)):
            found = False
            for i in range(length, len(data)):
                numbers = [data[d] for d in range(i-length, i)]

                if sum(numbers) == number:
                    found = True
                    break
            if found:
                print(min(numbers) + max(numbers))
                break
        break