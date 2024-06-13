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
    if op == "+":
        return summ(num1, num2)
    if op == "-":
        return dif(num1, num2)
    if op == "*":
        return mul(num1, num2)
    if op == ":":
        return div(num1, num2)
    return "Введен некорректный оператор"


# firstNumber = int(input("Введите первое число: "))
# secondNumber = int(input("Введите второе число: "))
# operand = input("Введите оператор: ")
#
# answer = calculator(firstNumber, secondNumber, operand)
#
# print("Ответ: ", answer)
