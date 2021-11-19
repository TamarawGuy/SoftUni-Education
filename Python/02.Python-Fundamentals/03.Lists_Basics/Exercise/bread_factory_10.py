energy = 100
coins = 100
is_bankrupt = False

line = input().split("|")
for event in line:
    tokens = event.split("-")
    task = tokens[0]
    amount = int(tokens[1])

    if task == "rest":
        if energy + amount > 100:
            print(f"You gained {100-energy} energy.")
            print(f"Current energy: {energy}.")
        else:
            energy += amount
            print(f"You gained {amount} energy.")
            print(f"Current energy: {energy}.")

    elif task == 'order':
        if energy < 30:
            energy += 50
            print("You had to rest!")
            continue
        
        coins += amount
        energy -= 30
        print(f"You earned {amount} coins.")

    else:
        if coins <= amount:
            print(f"Closed! Cannot afford {task}.")
            is_bankrupt = True
            break
        
        coins -= amount
        print(f"You bought {task}.")

if not is_bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")