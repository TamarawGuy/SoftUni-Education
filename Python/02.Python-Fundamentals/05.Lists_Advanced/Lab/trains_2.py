wagons = int(input())
l = [0] * wagons

while True:
    line = input().split(" ")
    if line[0] == 'End':
        break

    if line[0] == 'add':
        number = int(line[1])
        l[-1] += number
    
    if line[0] == 'insert':
        index = int(line[1])
        number = int(line[2])
        l[index] = l[index] + number

    if line[0] == 'leave':
        index = int(line[1])
        number = int(line[2])
        l[index] = l[index] - number
    
print(l)