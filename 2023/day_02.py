import argparse
import pathlib

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

games = {}
with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    for line in lines:
        game, sets = line.split(": ")
        game_id = game.split(" ")[1]
        games[game_id] = []
        for set in sets.split("; "):
            games[game_id].append({})
            for cubes in set.split(", "):
                n, cube = cubes.split(" ")
                games[game_id][-1][cube] = int(n)
# pprint(games)


def part_1():
    max_red = 12
    max_green = 13
    max_blue = 14

    result = 0
    for game_id, game in games.items():
        valid = True
        for set in game:
            if set.get("red", 0) > max_red or set.get("green", 0) > max_green or set.get("blue", 0) > max_blue:
                valid = False
        if valid:
            result += int(game_id)

    return result


def part_2():
    result = 0
    for game_id, game in games.items():
        red = max([set.get("red", 0) for set in game])
        green = max([set.get("green", 0) for set in game])
        blue = max([set.get("blue", 0) for set in game])

        result += red * green * blue

    return result


if args.part == 1:
    print(part_1())
else:
    print(part_2())
