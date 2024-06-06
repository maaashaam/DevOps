def sum(a, b):
    return a + b

def dif(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a // b

def calculator(a, b, oper):
    if oper == "+":
        return sum(a, b)
    if oper == "-":
        return dif(a, b)
    if oper == "*":
        return mul(a, b)
    if oper == ":":
        return div(a, b)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
oper = input("Введите оператор: ")

ans = calculator(a, b, oper)

print("Ответ: ", ans)