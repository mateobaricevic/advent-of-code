from argparse import ArgumentParser
from pathlib import Path

from numpy import array, linalg

path = Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()


class Game:
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize

    def __repr__(self):
        d = {
            "a": self.a,
            "b": self.b,
            "prize": self.prize,
        }
        return str(d)


games: list[Game] = []
with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    lines.append("")
    for i, line in enumerate(lines):
        if i % 4 == 0:
            a = line.split(": ")[1].split(", ")
            a = [int(n[2:]) for n in a]
        elif i % 4 == 1:
            b = line.split(": ")[1].split(", ")
            b = [int(n[2:]) for n in b]
        elif i % 4 == 2:
            prize = line.split(": ")[1].split(", ")
            prize = [int(n[2:]) for n in prize]
        else:
            games.append(Game(a, b, prize))
    # pprint(games)


def part_1():
    result = 0
    for game in games:
        cheapest = 10000000000000
        x, y = -1, -1
        for i in range(100):
            for j in range(100):
                if i * game.a[0] + j * game.b[0] == game.prize[0] and i * game.a[1] + j * game.b[1] == game.prize[1]:
                    if i * 3 + j < cheapest:
                        x = i
                        y = j
                        cheapest = i * 3 + j
        if cheapest < 10000000000000:
            result += cheapest
        print(cheapest, x, y)
    return result


def part_2():
    for game in games:
        game.prize[0] += 10000000000000
        game.prize[1] += 10000000000000

    result = 0
    for game in games:
        A = array([[game.a[0], game.b[0]], [game.a[1], game.b[1]]])
        y = array([game.prize[0], game.prize[1]])
        x, y = linalg.solve(A, y)
        x = int(round(x, 0))
        y = int(round(y, 0))
        if (
            x * game.a[0] + y * game.b[0] == game.prize[0]
            and x * game.a[1] + y * game.b[1] == game.prize[1]
        ):
            result += x * 3 + y
    return result


if args.part == 1:
    print(part_1())
else:
    print(part_2())
