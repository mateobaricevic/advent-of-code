
file = open("input.txt", 'r')

groups = file.read().split("\n\n")
nums = []
for i in range(0, len(groups)):
    groups[i] = set(groups[i].replace('\n', ''))
    nums.append(len(groups[i]))

print(sum(nums))
