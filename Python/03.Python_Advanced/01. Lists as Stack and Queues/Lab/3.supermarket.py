from collections import deque


my_d = deque()
while True:
    name = input()

    if name == "End":
        break

    elif name == "Paid":
        while len(my_d) > 0:
            n = my_d.pop()
            print(n)
    else:
        my_d.appendleft(name)


print(f"{len(my_d)} people remaining.")
