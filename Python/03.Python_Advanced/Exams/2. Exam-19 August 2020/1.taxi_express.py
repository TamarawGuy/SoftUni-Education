from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = deque([int(x) for x in input().split(", ")])
total_time = 0

while len(customers) > 0 and len(taxis) > 0:
    customer = customers.popleft()
    taxi = taxis.pop()

    if taxi >= customer:
        total_time += customer

    elif taxi < customer:
        customers.appendleft(customer)


if not customers and not taxis:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")

elif not customers:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")

elif not taxis:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, customers))}")