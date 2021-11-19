from collections import deque


def check_if_bomb_pouch_is_filled(d, c, s):
    if d >= 3 and c >= 3 and s >= 3:
        return True
    return False


def count_bombs(d, c, s):
    bomb_dict = {}

    bomb_dict["Datura Bombs"] = d
    bomb_dict["Cherry Bombs"] = c
    bomb_dict["Smoke Decoy Bombs"] = s

    sorted_dict = dict(sorted(bomb_dict.items(), key=lambda x: x[0]))
    
    return sorted_dict


bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = deque([int(x) for x in input().split(", ")])
daruta_bombs = 0
cherry_bombs = 0
smoke_bombs = 0
is_filled = False

while len(bomb_effects) > 0 and len(bomb_casings) > 0 and not is_filled:
    effect = bomb_effects.popleft()
    case = bomb_casings.pop()

    if effect + case == 40:
        daruta_bombs += 1

        if check_if_bomb_pouch_is_filled(daruta_bombs, cherry_bombs, smoke_bombs):
            is_filled = True
    
    elif effect + case == 60:
        cherry_bombs += 1

        if check_if_bomb_pouch_is_filled(daruta_bombs, cherry_bombs, smoke_bombs):
            is_filled = True
    
    elif effect + case == 120:
        smoke_bombs += 1

        if check_if_bomb_pouch_is_filled(daruta_bombs, cherry_bombs, smoke_bombs):
            is_filled = True
    
    else:
        bomb_effects.appendleft(effect)
        case -= 5
        bomb_casings.append(case)


b_dict = count_bombs(daruta_bombs, cherry_bombs, smoke_bombs)

if is_filled:
    print(f"Bene! You have successfully filled the bomb pouch!")
    
    if bomb_effects:
        res = ", ".join(map(str, bomb_effects))
        print(f"Bomb Effects: {res}")
    else:
        print("Bomb Effects: empty")

    if bomb_casings:
        res = ", ".join(map(str, bomb_casings))
        print(f"Bomb Casings: {res}")
    else:
        print("Bomb Casings: empty")
    
    for key, value in b_dict.items():
        print(f"{key}: {value}")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

    if bomb_effects:
        res = ", ".join(map(str, bomb_effects))
        print(f"Bomb Effects: {res}")
    else:
        print("Bomb Effects: empty")

    if bomb_casings:
        res = ", ".join(map(str, bomb_casings))
        print(f"Bomb Casings: {res}")
    else:
        print("Bomb Casings: empty")
    
    for key, value in b_dict.items():
        print(f"{key}: {value}")