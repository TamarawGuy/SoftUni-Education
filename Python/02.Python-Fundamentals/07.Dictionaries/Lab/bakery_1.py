line = input().split(" ")
bakery = {}

for i in range(0, len(line), 2):
    bakery[line[i]] = int(line[i+1])

print(bakery)