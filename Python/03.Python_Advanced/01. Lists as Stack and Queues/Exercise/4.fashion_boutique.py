numbers = [int(x) for x in input().split()]
capacity_of_rack = int(input())

racks = 1
my_sum = 0

while len(numbers) > 0:
    item = numbers[-1]
    
    if my_sum + item > capacity_of_rack:
        racks += 1
        my_sum = 0

    elif my_sum + item < capacity_of_rack:
        clothing = numbers.pop()
        my_sum += item

    elif my_sum + item == capacity_of_rack:
        clothing = numbers.pop()
        racks += 1
        my_sum = 0

print(racks)