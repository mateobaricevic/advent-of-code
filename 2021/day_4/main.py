
with open("2021/day04/input.txt") as file:
  content = file.read().split("\n\n")
  numbers = [
    int(number)
    for number in content[0].split(",")
  ]
  # print(numbers)
  
  boards = [
    [
      [
        int(number)
        for number in row.strip().replace("  ", " ").split(" ")
      ]
      for row in board.split("\n") if row != ""
    ]
    for board in content[1:]
  ]
  # print(boards)

# Part 1
# winner = -1
# for number in numbers:
#   for board in boards:
#     for row in board:
#       for i, num in enumerate(row):
#         if num == number:
#           row[i] = -1
  
#   for j, board in enumerate(boards):
#     for i, row in enumerate(board):
#       column = [row[i] for row in board]
#       if row.count(-1) == 5 or column.count(-1) == 5:
#         winner = j
#         break
#     else:
#       continue
#     break
#   else:
#     continue
#   break
# # print(number)
# # print(board[winner])

# sum = 0
# for row in boards[winner]:
#   for n in row:
#     if n != -1:
#       sum += n
# # print(sum)
# print(sum * number)

# Part 2
winners = [i for i in range(len(boards))]
for number in numbers:
  for board in boards:
    for row in board:
      for i, num in enumerate(row):
        if num == number:
          row[i] = -1
  
  for j, board in enumerate(boards):
    for i, row in enumerate(board):
      column = [row[i] for row in board]
      if row.count(-1) == 5 or column.count(-1) == 5:
        if j in winners:
          if len(winners) == 1:
            break
          winners.remove(j)
    else:
      continue
    break
  else:
    continue
  break
# print(number)
# print(boards[winners[0]])

sum = 0
for row in boards[winners[0]]:
  for n in row:
    if n != -1:
      sum += n
# print(sum)
print(sum * number)
