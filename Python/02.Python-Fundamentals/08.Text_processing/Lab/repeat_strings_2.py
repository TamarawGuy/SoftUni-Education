line = input().split(" ")
s = ''

for word in line:
    n = len(word)
    s += word * n

print(s)