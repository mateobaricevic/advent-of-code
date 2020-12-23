
file = open("input.txt")

input = file.read().split("\n\n")
input = [m.split("\n") for m in input]
rules = {}
for rule in input[0]:
    r = rule.split(": ")
    if "\"" in r[1]:
        rules[r[0]] = r[1].replace("\"", "")
    else:
        a = r[1].split(" | ")
        rules[r[0]] = [b.split(" ") for b in a]

messages = input[1]

def generate(rule_key):
    result = []
    rule = rules[rule_key]
    if type(rule) == str:
        return [rule]
    for r in rule:
        p = None
        for value in r:
            if p is None:
                p = generate(value)
            else:
                g = generate(value)
                newp = [vp + vg for vp in p for vg in g]
                p = newp
        result += p
    return result

possible = generate("0")
print(sum([1 for m in messages if m in possible]))
