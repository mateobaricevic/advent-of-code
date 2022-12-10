
with open('2019/day_8/input.txt', 'r') as input_file:
    image = input_file.read().splitlines()[0]
    # print(image)

length = 25
height = 6

layers = [image[i:i + length * height] for i in range(0, len(image) - length + 1, length * height)]

# print(layers)

fewest_zeros = length * height
fewest_layer = ''
for layer in layers:
    if layer.count('0') < fewest_zeros:
        fewest_zeros = layer.count('0')
        fewest_layer = layer

# print(fewest_layer)
print(fewest_layer.count('1') * fewest_layer.count('2'))