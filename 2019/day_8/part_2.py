
with open('2019/day_8/input.txt', 'r') as input_file:
    image = input_file.read().splitlines()[0]
    # print(image)

length = 25
height = 6

layers = [image[i:i + length * height] for i in range(0, len(image) - length + 1, length * height)]

# print(layers)

full_image = ['x' for _ in range(length * height)]
for layer in layers:
    for i, pixel in enumerate(layer):
        if pixel != '2' and full_image[i] == 'x':
            full_image[i] = pixel

for i, pixel in enumerate(full_image):
    print('o' if pixel == '1' else ' ', end='')
    if (i + 1) % length == 0:
        print()