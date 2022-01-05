
report = [ "00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010" ]
# with open("2021/day03/input.txt", "r") as file:
#   report = file.read().splitlines()


def getCounts():
  counts = [
    {
      "0": 0,
      "1": 0,
    }
    for _ in range(0, len(report[0]))
  ]
  for binary in report:
    for i, digit in enumerate(binary):
      counts[i][digit] += 1
  return counts

counts = getCounts()
# print(counts)

gamma = "".join(["0" if count["0"] > count["1"] else "1" for count in counts])
epsilon = "".join(["0" if x == "1" else "1" for x in gamma])
print(int(gamma, 2), int(epsilon, 2))
print(int(gamma, 2) * int(epsilon, 2))

# Part 2
oxygen = report[:]
for i in range(0, len(counts)):
  delete = []
  if counts[i]["0"] > counts[i]["1"]:
    for j in range(0, len(oxygen)):
      if oxygen[j][i] != "0":
        delete.append(oxygen[j])
  else:
    for j in range(0, len(oxygen)):
      if oxygen[j][i] != "1":
        delete.append(oxygen[j])
  for d in delete:
    oxygen.remove(d)
    if len(oxygen) == 1:
      break
  if len(oxygen) == 1:
    break
  counts = getCounts()
oxygen = oxygen[0]

co2 = report[:]
for i in range(0, len(counts)):
  delete = []
  if counts[i]["0"] <= counts[i]["1"]:
    for j in range(0, len(co2)):
      if co2[j][i] != "0":
        delete.append(co2[j])
  else:
    for j in range(0, len(co2)):
      if co2[j][i] != "1":
        delete.append(co2[j])
  for d in delete:
    co2.remove(d)
    if len(co2) == 1:
      break
  if len(co2) == 1:
    break
  counts = getCounts()
co2 = co2[0]

print(oxygen, co2)
print(int(oxygen, 2), int(co2, 2))
print(int(oxygen, 2) * int(co2, 2))
