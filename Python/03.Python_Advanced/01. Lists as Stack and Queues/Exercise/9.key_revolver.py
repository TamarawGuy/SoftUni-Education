from collections import deque

price_of_each_bullet = int(input())
gun_barrel_size = int(input())
gun_barrel_size_copy = gun_barrel_size
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())
used_bullets = 0
success = True

while locks:
    
    current_bullet = bullets.pop()
    current_lock = locks[0]

    if current_bullet > current_lock:
        gun_barrel_size_copy -= 1
        used_bullets += 1
        print("Ping!")

        if locks and not bullets:
            success = False
            break
        
        if not locks and not bullets:
            break

        if gun_barrel_size_copy == 0:
            gun_barrel_size_copy = gun_barrel_size
            print("Reloading!")

    elif current_bullet <= current_lock:
        locks.popleft()
        gun_barrel_size_copy -= 1
        used_bullets += 1
        print("Bang!")
    
        if locks and not bullets:
            success = False
            break

        if not locks and not bullets:
            break

        if gun_barrel_size_copy == 0:
            gun_barrel_size_copy = gun_barrel_size
            print("Reloading!")


if success:
    price = used_bullets * price_of_each_bullet
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - price}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")