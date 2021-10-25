numbers = [int(x) for x in input().split(" ")]
n = int(input())

for i in range(n):
    min_number = min(numbers)
    numbers.remove(min_number)

print(numbers)