import argparse
import pathlib

path = pathlib.Path(__file__)
input_file = f'{path.parent}/inputs/{path.stem}.txt'

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default=input_file)
parser.add_argument('-p', '--part', type=int, choices=[1, 2], default=1)
args = parser.parse_args()

with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    image = lines[0]


def part_1():
    length = 25
    height = 6

    layers = [
        image[i : i + length * height] for i in range(0, len(image) - length + 1, length * height)
    ]
    # print(layers)

    fewest_zeros = length * height
    fewest_layer = ''
    for layer in layers:
        if layer.count('0') < fewest_zeros:
            fewest_zeros = layer.count('0')
            fewest_layer = layer
    # print(fewest_layer)

    return fewest_layer.count('1') * fewest_layer.count('2')


def part_2():
    length = 25
    height = 6

    layers = [
        image[i : i + length * height] for i in range(0, len(image) - length + 1, length * height)
    ]
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


if args.part == 1:
    print(part_1())
else:
    part_2()
