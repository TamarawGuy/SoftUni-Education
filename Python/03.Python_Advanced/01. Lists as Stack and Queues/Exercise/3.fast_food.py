from collections import deque

quanitity = int(input())
numbers = deque([int(x) for x in input().split()])

print(max(numbers))

while numbers and quanitity > 0:
    client = numbers[0]
    if quanitity - client > 0:
        quanitity -= client
        person = numbers.popleft()
    else:
        break

if numbers:
    print(f"Orders left: {' '.join(map(str, numbers))}")
else:
    print("Orders complete")