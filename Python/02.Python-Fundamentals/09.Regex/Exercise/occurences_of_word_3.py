import re

data = input()
searched = input()

pattern = f"\\b{searched}\\b"

res = re.findall(pattern, data, re.IGNORECASE)

print(len(res))