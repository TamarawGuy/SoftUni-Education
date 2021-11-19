from collections import deque

stations = deque()
n = int(input())

for _ in range(n):
    stations.append([el for el in input().split()])

for big_circle in range(n):
    is_valid = True
    tank = 0

    for small_circle in range(n):
        tank += int(stations[small_circle][0]) - int(stations[small_circle][1])

        if tank < 0:
            is_valid = False
            stations.append(stations.popleft())
            break
    
    if is_valid:
        print(big_circle)
        break