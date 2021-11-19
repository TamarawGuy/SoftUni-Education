from collections import deque

jobs = deque([int(x) for x in input().split(", ")])
job_index = int(input())
clock_cycles = 0
found = False
index = -1

while not found:
    index += 1
    for item in jobs:
        if index == item:
            item_index = jobs.index(item)
            if item_index == job_index:
                found = True
                clock_cycles += index
                break
            
            else:
                clock_cycles += index
                jobs[item_index] = -1

print(clock_cycles)