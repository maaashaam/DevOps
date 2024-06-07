"""
The code implements a simple calculator with four operations(+, -, *, :)
"""


def summ(a, b):
    """Return the sum of numbers"""
    return a + b


def dif(a, b):
    """Return the difference of numbers"""
    return a - b


def mul(a, b):
    """Return the multiplication of numbers"""
    return a * b


def div(a, b):
    """Return the division of numbers"""
    return a // b


def calculator(num1, num2, op):
    """Return the result of expression"""
    result = 0
    if op == "+":
        result = summ(num1, num2)
        return result
    if op == "-":
        result = dif(num1, num2)
        return result
    if op == "*":
        result = mul(num1, num2)
        return result
    if op == ":":
        result = div(num1, num2)
        return result


firstNumber = int(input("Введите первое число: "))
secondNumber = int(input("Введите второе число: "))
operand = input("Введите оператор: ")

answer = calculator(firstNumber, secondNumber, operand)

print("Ответ: ", answer)
