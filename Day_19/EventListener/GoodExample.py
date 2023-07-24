def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(n1, n2, func):
    return func(n1, n2)


print(calculator(10, 2, add))
print(calculator(10, 2, subtract))
print(calculator(10, 2, multiply))
print(calculator(10, 2, divide))