from collections import deque

def next_second(h, m, s):
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0
    
    return h, m, s

robot_info = input().split(";")
robot_dict = {}
available_robots = deque()
waiting_robots = deque()
products = deque()

time = [int(x) for x in input().split(":")]

while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

for robot in robot_info:
    r = robot.split("-")
    robot_name = r[0]
    robot_time = int(r[1])
    available_robots.append([robot_name, robot_time])
    robot_dict[robot_name] = robot_time

while products:
    for robot in waiting_robots:
        r_name = robot[0]
        robot[1] -= 1
        if robot[1] <= 0:
            available_robots.append([r_name, robot_dict[r_name]])
    
    waiting_robots = [r for r in waiting_robots if r[1] > 0]

    time = next_second(time[0], time[1], time[2])
    current_product = products.popleft()

    if not available_robots:
        products.append(current_product)
        continue

    current_robot = available_robots.popleft()
    print(f"{current_robot[0]} - {current_product} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]")
    waiting_robots.append(current_robot)