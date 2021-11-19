line = input().split(", ")
text = input()

for word in line:
    length = len(word)
    replaced = '*' * length
    text = text.replace(word, replaced)

print(text)