minute = int(input())
second = int(input())

second += 15

if second >= 60:
    minute += 1
    second -= 60

if minute == 24:
    minute = 0

print(f"{minute}:{second:02d}")