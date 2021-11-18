word = list(input())

d = {}

for char in word:
    if char not in d and char != " ":
        d[char] = 1
    elif char in d and char != " ":
        d[char] += 1

for key, value in d.items():
    print(f"{key} -> {value}")   