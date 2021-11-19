from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_water = deque([int(x) for x in input().split()])
copy_cups_capacity = deque([x for x in cups_capacity])
copy_bottles_water = deque([x for x in bottles_water])
wasted_water = 0


while copy_cups_capacity:
    if not copy_bottles_water:
        break
    current_water_bottle = copy_bottles_water[-1]
    current_cup = copy_cups_capacity[0]
    
    if current_water_bottle >= current_cup:
        wasted_water += current_water_bottle - current_cup
        current_water_bottle = copy_bottles_water.pop()
        current_cup = copy_cups_capacity.popleft()

    elif current_water_bottle < current_cup:
        add_to_last_bottle = copy_bottles_water.pop()
        copy_bottles_water[-1] += add_to_last_bottle
        continue


while cups_capacity:
    if not bottles_water:
        break
    current_water_bottle = bottles_water[-1]
    current_cup = cups_capacity[0]

    if current_water_bottle >= current_cup:
        current_water_bottle -= current_cup
        bottles_water[-1] = current_water_bottle
        cups_capacity.popleft()
        if bottles_water[-1] <= 0:
            del bottles_water[-1]
    elif current_water_bottle < current_cup:
        current_cup -= current_water_bottle
        bottles_water.pop()


if not cups_capacity:
    print(f"Bottles: {len(bottles_water)}")
else:
    print(f"Cups: {' '.join(map(str, copy_cups_capacity))}")

print(f"Wasted litters of water: {wasted_water}")
