s1 = input()
s2 = input()

while s1 in s2:
    s2 = s2.replace(s1, "")

print(s2)