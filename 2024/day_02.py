import argparse
import pathlib

path = pathlib.Path(__file__)
input_file = f"{path.parent}/inputs/{path.stem}.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default=input_file)
parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=1)
args = parser.parse_args()

reports = []
with open(args.input) as input_file:
    lines = input_file.read().splitlines()
    for line in lines:
        report = [int(n) for n in line.split(" ")]
        reports.append(report)
# pprint(reports)


def part_1():
    result = 0
    for report in reports:
        trend = report[0] > report[1]

        safe = True
        n = report.pop(0)
        while len(report) > 0:
            n_2 = report.pop(0)
            if not (1 <= abs(n_2 - n) <= 3) or (n > n_2) != trend:
                safe = False
                break
            n = n_2
        if safe:
            result += 1

    return result


def check(report, removed=False):
    trend = report[0] > report[1]

    i = 0
    while i < len(report) - 1:
        n = report[i]
        n_2 = report[i + 1]
        if not (1 <= abs(n - n_2) <= 3) or (n > n_2) != trend:
            if not removed:
                for i in range(len(report)):
                    report_copy = report.copy()
                    report_copy.pop(i)
                    if check(report_copy, True):
                        return True
            return False
        i += 1
    return True


def part_2():
    result = 0
    for report in reports:
        if check(report):
            result += 1

    return result


if args.part == 1:
    print(part_1())
else:
    print(part_2())
