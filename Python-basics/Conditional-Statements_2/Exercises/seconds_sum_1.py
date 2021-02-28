seconds_1 = int(input())
seconds_2 = int(input())
seconds_3 = int(input())
minutes = 0
total_seconds = seconds_1 + seconds_2 + seconds_3

while total_seconds > 60:
    minutes += 1
    total_seconds -= 60

print(f"{minutes}:{total_seconds:02d}")