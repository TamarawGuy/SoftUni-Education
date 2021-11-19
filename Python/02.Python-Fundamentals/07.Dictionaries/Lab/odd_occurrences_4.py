line = [x.lower() for x in input().split(" ")]

d = {}

for item in line:
    if item not in d:
        d[item] = 1
    else:
        d[item] += 1

for key, value in d.items():
    if value % 2 == 1:
        print(key, end=" ")