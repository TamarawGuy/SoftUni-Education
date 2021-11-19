from collections import deque

my_d = deque()
quantity = int(input())

while True:
    name = input()
    if name == "Start":
        break

    my_d.appendleft(name)


while True:
    command = input().split()
    if command[0] == 'End':
        break

    elif command[0].isdigit():
        water = int(command[0])

        if water > quantity:
            name = my_d.pop()
            print(f"{name} must wait")
        else:
            quantity -= water
            name = my_d.pop()
            print(f"{name} got water")
    
    elif command[0] == 'refill':
        water = int(command[1])
        quantity += water
    

print(f"{quantity} liters left")