
# numbers = [0, 3, 6]
numbers = [13, 16, 0, 12, 15, 1]
# last = {0: 1, 3: 2}
last = {13: 1, 16: 2, 0: 3, 12: 4, 15: 5}

while len(numbers) < 30000001:
    n = numbers[len(numbers)-1]
    next_n = 0
    if n in last:
        next_n = len(numbers) - last[n]
    numbers.append(next_n)
    last[n] = len(numbers)-1
    if len(numbers) % 3000000 == 0:
        print("{:.0f}% done.".format(len(numbers)/30000001*100))

print(numbers[2019])
print(numbers[29999999])
