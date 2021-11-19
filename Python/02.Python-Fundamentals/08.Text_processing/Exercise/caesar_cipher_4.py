line = list(input())
encrypted = []

for ch in line:
    number = ord(ch)
    number += 3
    new_ch = chr(number)
    encrypted.append(new_ch)

print("".join(encrypted))