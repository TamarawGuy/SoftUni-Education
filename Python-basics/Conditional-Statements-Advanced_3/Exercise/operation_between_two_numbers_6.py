n1 = int(input())
n2 = int(input())
operator = input()
odd_or_even = ""

if n2 != 0:
    if operator == "+":
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    elif operator == '*':
        result = n1 * n2
    elif operator == '/':
        result = n1 / n2
    
    if result % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
        print(f"{n1} {operator} {n2} = {result} - {odd_or_even}")

else:
    print(f"Cannot divide {n1} by zero")