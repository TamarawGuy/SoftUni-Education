line = list(input())
valid = False
new_s = ''
last_letter = line[-1]

for i in range(1, len(line)):
    if line[i-1] != line[i]:
        letter = line[i-1]
        new_s += letter


print(new_s + last_letter)