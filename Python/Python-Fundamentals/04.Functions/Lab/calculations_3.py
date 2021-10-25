op = input()
n1 = int(input())
n2 = int(input())

def calculate(operator, num1, num2):
    if operator == "add":
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2
    elif operator == 'multiply':
        return  num1 * num2
    elif operator == 'divide':
        return num1 // num2
    
print(calculate(op, n1, n2))