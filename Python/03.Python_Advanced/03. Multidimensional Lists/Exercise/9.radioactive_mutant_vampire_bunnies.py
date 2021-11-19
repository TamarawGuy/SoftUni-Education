from collections import deque

def read_matrix():
    matrix = []

    for _ in range(rows):
        line = list(input())
        matrix.append(line)
    
    return matrix


def find_player_coordinates(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "P":
                return r, c


def collect_bunny_coordinates(matrix):
    bunny_coordinates = []

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "B":
                bunny_coordinates.append((r, c))
    
    return bunny_coordinates


def check_valid_coordinates_for_bunny_replication(matrix, r, c):
    if 0 <= r < rows and 0 <= c < cols and matrix[r][c] == ".":
        return True

    elif 0 <= r < rows and 0 <= c < cols and matrix[r][c] == "B":
        return False
    
    elif 0 <= r < rows and 0 <= c < cols and matrix[r][c] == "P":
        dead = True
        return True

def check_if_player_escaped(r, c):
    if 0 <= r < rows and 0 <= c < cols:
        return False
    return True


def check_if_player_encoutered_enemy(matrix, r, c):
    if matrix[r][c] == "B":
        return True

    return False


def check_if_bunny_encoutered_player(matrix, r, c):
    if matrix[r][c] == "P":
        return True
    return False


def bunny_replication(matrix, bunny_coordinates):
    for coordinates in bunny_coordinates:
        bunny_row = coordinates[0]
        bunny_col = coordinates[1]

        if check_valid_coordinates_for_bunny_replication(matrix, bunny_row-1, bunny_col):
            matrix[bunny_row-1][bunny_col] = "B"
        

        if check_valid_coordinates_for_bunny_replication(matrix, bunny_row+1, bunny_col):
            matrix[bunny_row+1][bunny_col] = "B"
        

        if check_valid_coordinates_for_bunny_replication(matrix, bunny_row, bunny_col-1):
            matrix[bunny_row][bunny_col-1] = "B"
        

        if check_valid_coordinates_for_bunny_replication(matrix, bunny_row, bunny_col+1):
            matrix[bunny_row][bunny_col+1] = "B"


    return matrix


rows, cols = [int(x) for x in input().split()]
m = read_matrix()
moving_commands = deque(list(input()))
start_row, start_col = find_player_coordinates(m)
dead = False
escaped = False

while len(moving_commands) > 0 and not dead and not escaped:
    command = moving_commands.popleft()
    enemy_coordinates = collect_bunny_coordinates(m)

    if command == "U":
        start_row -= 1

        if check_if_player_escaped(start_row, start_col):
            start_row += 1
            m[start_row][start_col] = "."
            escaped = True

        elif check_if_player_encoutered_enemy(m, start_row, start_col):
            dead = True
        
        else:
            m[start_row+1][start_col] = "."
            m[start_row][start_col] = 'P'
            bunny_replication(m, enemy_coordinates)
            if dead:
                start_row += 1

    elif command == "R":
        start_col += 1
        
        if check_if_player_escaped(start_row, start_col):
            start_col -= 1
            m[start_row][start_col] = "."
            escaped = True

        elif check_if_player_encoutered_enemy(m, start_row, start_col):
            dead = True

        else:
            m[start_row][start_col-1] = "."
            m[start_row][start_col] = 'P'
            bunny_replication(m, enemy_coordinates)
            if dead:
                start_col -= 1


    elif command == "D":
        start_row += 1

        if check_if_player_escaped(start_row, start_col):
            start_row -= 1
            m[start_row][start_col] = "."
            escaped = True
            break

        elif check_if_player_encoutered_enemy(m, start_row, start_col):
            dead = True
            break
        
        else:
            m[start_row-1][start_col] = "."
            m[start_row][start_col] = 'P'
            bunny_replication(m, enemy_coordinates)
            if dead:
                start_row -= 1
                break

    elif command == "L":
        start_col -= 1

        if check_if_player_escaped(start_row, start_col):
            start_col += 1
            m[start_row][start_col] = "."
            escaped = True
            break

        elif check_if_player_encoutered_enemy(m, start_row, start_col):
            dead = True
            break
        
        else:
            m[start_row][start_col+1] = "."
            m[start_row][start_col] = 'P'
            bunny_replication(m, enemy_coordinates)
            if dead:
                start_col += 1
                break

if dead:
    bunny_replication(m, enemy_coordinates)
    for row in m:
        print("".join(row))
    print(f"dead: {start_row} {start_col}")

elif escaped:
    bunny_replication(m, enemy_coordinates)
    for row in m:
        print("".join(row))
    print(f"won: {start_row} {start_col}")