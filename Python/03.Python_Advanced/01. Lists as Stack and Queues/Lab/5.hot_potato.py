from collections import deque

line = deque(input().split())
toss = int(input())

while len(line) > 1:
    line.rotate(-(toss-1))
    name = line.popleft()
    print(f"Removed {name}")

print(*line)