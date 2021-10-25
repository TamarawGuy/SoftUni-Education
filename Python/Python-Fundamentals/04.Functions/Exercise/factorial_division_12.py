def fac1(num1):
    res = 1
    for i in range(1, num1+1):
        res *= i
    return res


def fac2(num2):
    res = 1
    for i in range(1, num2+1):
        res *= i
    return res

n1 = int(input())
n2 = int(input())
number1 = fac1(n1)
number2 = fac2(n2)
result = number1 / number2
print(f"{result:.2f}")