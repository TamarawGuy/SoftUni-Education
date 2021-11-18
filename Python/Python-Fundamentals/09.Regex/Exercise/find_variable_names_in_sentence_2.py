import re

data = input()
pattern = r"((?<=^_)|(?<=\s_))[A-Za-z0-9]+\b"

result = re.finditer(pattern, data)
res = [x.group() for x in result]
print(*res, sep=",")