
file = open("input.txt", 'r')

groups = file.read().split("\n\n")

nums = []
for i in range(0, len(groups)):
    answers = groups[i].split('\n')

    chars = []
    for char in answers[0]:
        has_char = []
        for answer in answers[1:]:
            has_char_a = False
            for char_a in answer:
                if char_a == char:
                    has_char_a = True
            if has_char_a:
                has_char.append(True)
            else:
                has_char.append(False)
        if all(has_char):
            chars.append(char)

    nums.append(len(chars))

print(sum(nums))
