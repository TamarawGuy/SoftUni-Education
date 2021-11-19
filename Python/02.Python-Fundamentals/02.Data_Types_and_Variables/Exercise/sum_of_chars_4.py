n = int(input())
sum = 0
for i in range(n):
    ch = input()
    value = ord(ch)
    sum += value

print(f"The sum equals: {sum}")