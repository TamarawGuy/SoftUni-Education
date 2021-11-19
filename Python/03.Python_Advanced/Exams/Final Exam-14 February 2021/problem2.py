from math import floor

def read_matrix():
    matrix = []
    for _ in range(size):
        line = input().split()
        matrix.append(line)

    return matrix


def get_player_coordinates(matrix):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "P":
                return r, c


def check_if_coordinates_are_valid(r, c):
    return 0 <= r < size and 0 <= c < size


def check_if_player_hits_wall(matrix, r, c):
    if matrix[r][c] == "X":
        return True
    
    return False

size = int(input())
m = read_matrix()
player_row, player_col = get_player_coordinates(m)
total_coins = 0
dead = False
coins_collected = False
collected_coins_coordinated = []

while not dead and not coins_collected:
    command = input()

    if command == 'up':
        player_row -= 1

        if check_if_coordinates_are_valid(player_row, player_col):
            if not check_if_player_hits_wall(m, player_row, player_col):
                coins = int(m[player_row][player_col])
                total_coins += coins
                coin_coordinates = [player_row, player_col]
                collected_coins_coordinated.append(coin_coordinates)

                if total_coins >= 100:
                    coins_collected = True
            
            else:
                dead = True
        
        else:
             dead = True

    elif command == 'right':
        player_col += 1

        if check_if_coordinates_are_valid(player_row, player_col):
            if not check_if_player_hits_wall(m, player_row, player_col):
                coins = int(m[player_row][player_col])
                total_coins += coins
                coin_coordinates = [player_row, player_col]
                collected_coins_coordinated.append(coin_coordinates)

                if total_coins >= 100:
                    coins_collected = True
            
            else:
                dead = True
        
        else:
            dead = True

    elif command == 'down':
        player_row += 1

        if check_if_coordinates_are_valid(player_row, player_col):
            if not check_if_player_hits_wall(m, player_row, player_col):
                coins = int(m[player_row][player_col])
                total_coins += coins
                coin_coordinates = [player_row, player_col]
                collected_coins_coordinated.append(coin_coordinates)

                if total_coins >= 100:
                    coins_collected = True
            
            else:
                dead = True
        
        else:
            dead = True

    elif command == 'left':
        player_col -= 1

        if check_if_coordinates_are_valid(player_row, player_col):
            if not check_if_player_hits_wall(m, player_row, player_col):
                coins = int(m[player_row][player_col])
                total_coins += coins
                coin_coordinates = [player_row, player_col]
                collected_coins_coordinated.append(coin_coordinates)

                if total_coins >= 100:
                    coins_collected = True
            
            else:
                dead = True
        else:
            dead = True

if dead:
    total_coins -= total_coins * 0.5
    total_coins = floor(total_coins)
    print(f"Game over! You've collected {total_coins} coins.")
    print(f"Your path:")
    for item in collected_coins_coordinated:
        print(item)

elif coins_collected:
    print(f"You won! You've collected {total_coins} coins.")
    print(f"Your path:")
    for item in collected_coins_coordinated:
        print(item)