import re

data = input()
pattern = r"\d+"
nums = []
while data:
    match = re.findall(pattern, data)
    if match:
        nums.extend(match)
    data = input()

print(*nums, sep=" ")