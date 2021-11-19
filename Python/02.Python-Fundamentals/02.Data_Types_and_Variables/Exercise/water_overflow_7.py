n = int(input())
sum = 0
for i in range(n):
    num = int(input())
    if sum + num > 255:
        print("Insufficient capacity!")
    else:
        sum += num
print(sum)