def add_and_subtract(num1, num2, num3):
    res = 0
    def sum_numbers():
        return num1 + num2

    
    def subtract():
        sum_of_first_two = sum_numbers()
        return sum_of_first_two - num3
    
    return subtract()

n1 = int(input())
n2 = int(input())
n3 = int(input())

print(add_and_subtract(n1, n2, n3))