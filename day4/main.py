import string

file = open("input.txt", 'r')

passports = []
for passport in file.read().split('\n\n'):
    passports.append(passport.replace('\n', ' ').split(' '))

count = 0
count2 = 0
for p in passports:
    num = 0
    num2 = 0
    for entry in p:
        # First part
        if entry[:3] == "byr":
            num += 1
        elif entry[:3] == "iyr":
            num += 1
        elif entry[:3] == "eyr":
            num += 1
        elif entry[:3] == "hgt":
            num += 1
        elif entry[:3] == "hcl":
            num += 1
        elif entry[:3] == "ecl":
            num += 1
        elif entry[:3] == "pid":
            num += 1

        # Second part
        if entry[:3] == "byr" and 1920 <= int(entry[4:]) <= 2002:
            num2 += 1
        elif entry[:3] == "iyr" and 2010 <= int(entry[4:]) <= 2020:
            num2 += 1
        elif entry[:3] == "eyr" and 2020 <= int(entry[4:]) <= 2030:
            num2 += 1
        elif entry[:3] == "hgt":
            if entry[-2:] == "cm" and 150 <= int(entry[4:len(entry)-2]) <= 193:
                num2 += 1
            elif entry[-2:] == "in" and 59 <= int(entry[4:len(entry)-2]) <= 76:
                num2 += 1
        elif entry[:3] == "hcl" and entry[4] == '#' and len(entry[5:]) == 6 and all(char in set(string.hexdigits) for char in entry[5:]):
            num2 += 1
        elif entry[:3] == "ecl" and any(i == entry[4:] for i in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            num2 += 1
        elif entry[:3] == "pid" and len(entry[4:]) == 9:
            num2 += 1
    if num == 7:
        count += 1
    if num2 == 7:
        count2 += 1

print(count, count2)