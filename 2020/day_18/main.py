
file = open("input.txt")

homework = file.read().split("\n")[:-1]

def order(operation):
    if operation == '+' or operation == '*':
        return 1
    return 0

def order2(operation):
    if operation == '*':
        return 1
    elif operation == '+':
        return 2
    return 0

def apply_operation(operation, a, b):
    if  operation == '+':
        return a + b
    elif operation == '*':
        return a * b

def evaluate(expression):
    values = []
    operations = []
    i = 0

    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue

        # print(values)
        # print(operations)
        if expression[i].isdigit():
            value = 0
            while i < len(expression) and expression[i].isdigit():
                value = (value * 10) + int(expression[i])
                i += 1

            values.append(value)
            continue
        elif expression[i] == '(':
            operations.append(expression[i])
        elif expression[i] == ')':
            while operations[-1] != '(':
                value2 = values.pop()
                value1 = values.pop()
                operation = operations.pop()

                values.append(apply_operation(operation, value1, value2))
            # Pop '('
            operations.pop()
        else:
            while len(operations) != 0 and order2(operations[-1]) >= order2(expression[i]):
                value2 = values.pop()
                value1 = values.pop()
                operation = operations.pop()

                values. append(apply_operation(operation, value1, value2))
            operations.append(expression[i])
        i += 1

    while len(operations) != 0:
        value2 = values.pop()
        value1 = values.pop()
        operation = operations.pop()

        values. append(apply_operation(operation, value1, value2))

    return values[-1]

# print(evaluate("5 + (8 * 3 + 9 + 3 * 4 * 3)"))

results = []
for expression in homework:
    result = evaluate(expression)
    results.append(result)

print(sum(results))
