line = input().split(" ")
s1 = list(line[0])
s2 = list(line[1])
sum = 0

if len(s1) <= len(s2):
    for i in range(len(s1)):
        number = ord(s1[i]) * ord(s2[i])
        sum += number

    left = len(s2) - len(s1)

    if left > 0:
        for i in range(left, 0, -1):
            sum += ord(s2[i])
        
else:
    for i in range(len(s2)):
        number = ord(s1[i]) * ord(s2[i])
        sum += number

    left = len(s1) - len(s2)

    if left > 0:
        for i in range(left, 0, -1):
            sum += ord(s1[i])

print(sum)