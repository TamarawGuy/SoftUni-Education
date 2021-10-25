s = [int(x) for x in input().split(" ")]
new_s = []

for item in s:
    new_s.append(item * -1)

print(new_s)