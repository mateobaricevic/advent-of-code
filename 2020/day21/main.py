import pprint

file = open("input.txt")
foods = file.read().split("\n")[:-1]
foods = [{"ingredients" : food.split(" (contains ")[0].split(" "),
          "allergens" : food.split(" (contains ")[1].replace(")", "").split(", ")} for food in foods]
# pprint.pprint(foods, width=58)

ingredients = {}
for food in foods:
    for ingredient in food["ingredients"]:
        if ingredient not in ingredients.keys():
            ingredients[ingredient] = ''
# print(ingredients)

def countOccurances(list):
    result = []
    unique = set(list)
    for item in unique:
        count = 0
        for i in range(len(list)):
            if list[i] == item:
                count += 1
        result.append((item, count))
    return result

for _ in range(2):
    for food in foods:
        for allergen in food["allergens"]:
            count = 1
            possibilities = food["ingredients"][:]
            for f in foods:
                if f == food:
                    continue
                if allergen in f["allergens"]:
                    possibilities += f["ingredients"]
                    count += 1
            counts = countOccurances(possibilities)
            possibilities = []
            for c in counts:
                if count == c[1]:
                    possibilities.append(c[0])
            if len(possibilities) == 1:
                ingredients[possibilities[0]] = allergen
                for foo in foods:
                    foo["allergens"] = list(filter(lambda a: a != allergen, foo["allergens"]))
                    foo["ingredients"] = list(filter(lambda i: i != possibilities[0], foo["ingredients"]))
            # print(allergen, possibilities)

# pprint.pprint(ingredients)

not_allergens = [i for i, s in ingredients.items() if s == '']
# print(not_allergens)

count = 0
for i in not_allergens:
    for food in foods:
        for ingredient in food["ingredients"]:
            if ingredient == i:
                count += 1
print(count)

allergens = [(s, i) for i, s in ingredients.items() if s != '']
allergens.sort()
# print(allergens)
print(",".join([i[1] for i in allergens]))
