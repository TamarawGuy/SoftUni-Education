line = [int(x) for x in input().split(', ')]
even_indeces = []

for i in range(len(line)):
    if line[i] % 2 == 0:
        even_indeces.append(i)

print(even_indeces)