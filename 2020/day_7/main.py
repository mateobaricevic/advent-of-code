import pprint

file = open("input.txt", 'r')

rules = file.read().split('\n')

# pprint.pprint(rules, width=200)

dictionary = {}
for rule in rules[:len(rules)-1]:
    rule_space = rule.split(' ')
    rule_comma = rule.split(',')
    if rule_space[4] != 'no':
        bags = [[' '.join(rule_bag.split(' ')[-3:-1]), int(rule_bag.split(' ')[-4])] for rule_bag in rule_comma]
        dictionary[' '.join(rule_space[0:2])] = {}
        for bag in bags:
            dictionary[' '.join(rule_space[0:2])][bag[0]] = bag[1]
    else:
        dictionary[' '.join(rule_space[0:2])] = 0

# pprint.pprint(dictionary)

bags = []
def countUp(bag):
    for key, value in dictionary.items():
        if type(value) is dict:
            for key2, value2 in value.items():
                if key2 == bag:
                    if key not in bags:
                        bags.append(key)
                        countUp(key)
countUp("shiny gold")
print(len(bags))

def countDown(bag):
    c = 0
    in_current_bag = dictionary[bag]

    if type(in_current_bag) is dict:
        for key, value in in_current_bag.items():
            c += value + value * countDown(key)
    return c

print(countDown("shiny gold"))
