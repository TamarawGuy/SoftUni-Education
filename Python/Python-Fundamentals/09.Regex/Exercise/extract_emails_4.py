import re

data = input()

pattern = r"(^|(?<=\s))[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+@[A-Za-z]+\-?[A-Za-z]+(\.[a-zA-z]+)+"

res = re.finditer(pattern, data)

for el in res:
    print(el.group())