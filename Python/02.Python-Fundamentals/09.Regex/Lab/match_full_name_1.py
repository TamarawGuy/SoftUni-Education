import re

data = input()
pattern = "\\b[A-Z][a-z]+ +[A-Z][a-z]+\\b"
names = re.findall(pattern, data)

print(*names)