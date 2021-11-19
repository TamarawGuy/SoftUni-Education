from collections import deque

def read_matrix():
    matrix = []

    for _ in range(field_size):
        line = list(input())
        line = [x for x in line if x != " "]
        matrix.append(line)
    
    return matrix


def find_character_place(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 's':
                return r, c


def calculate_all_coals_in_the_field(matrix):
    coals = 0

    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 'c':
                coals += 1
    
    return coals


def check_if_coordinates_are_valid(r, c):
    return 0 <= r < field_size and 0 <= c < field_size


field_size = int(input())
moving_commands = deque(input().split(" "))
matrix = read_matrix()

all_coals = calculate_all_coals_in_the_field(matrix)
coals_collected = 0
start_row, start_col = find_character_place(matrix)
game_over = False
all_coals_are_collected = False

while len(moving_commands) > 0:
    command = moving_commands.popleft()
    
    if command == 'up':
        start_row -= 1
        if check_if_coordinates_are_valid(start_row, start_col):
            if matrix[start_row][start_col] == 'c':
                matrix[start_row][start_col] = '*'
                coals_collected += 1
                if coals_collected == all_coals:
                    all_coals_are_collected = True
                    print(f"You collected all coals! ({start_row}, {start_col})")
                    break
        
            elif matrix[start_row][start_col] == 'e':
                game_over = True
                print(f"Game over! ({start_row}, {start_col})")
                break
        else:
            start_row += 1

    elif command == 'right':
        start_col += 1
        if check_if_coordinates_are_valid(start_row, start_col):
            if matrix[start_row][start_col] == 'c':
                matrix[start_row][start_col] = '*'
                coals_collected += 1
                if coals_collected == all_coals:
                    all_coals_are_collected = True
                    print(f"You collected all coals! ({start_row}, {start_col})")
                    break
        
            elif matrix[start_row][start_col] == 'e':
                game_over = True
                print(f"Game over! ({start_row}, {start_col})")
                break
        else:
            start_col -= 1

    elif command == 'down':
        start_row += 1
        if check_if_coordinates_are_valid(start_row, start_col):
            if matrix[start_row][start_col] == 'c':
                matrix[start_row][start_col] = '*'
                coals_collected += 1
                if coals_collected == all_coals:
                    all_coals_are_collected = True
                    print(f"You collected all coals! ({start_row}, {start_col})")
                    break
        
            elif matrix[start_row][start_col] == 'e':
                game_over = True
                print(f"Game over! ({start_row}, {start_col})")
                break
        else:
            start_row -= 1

    elif command == 'left':
        start_col -= 1
        if check_if_coordinates_are_valid(start_row, start_col):
            if matrix[start_row][start_col] == 'c':
                matrix[start_row][start_col] = '*'
                coals_collected += 1
                if coals_collected == all_coals:
                    all_coals_are_collected = True
                    print(f"You collected all coals! ({start_row}, {start_col})")
                    break
        
            elif matrix[start_row][start_col] == 'e':
                game_over = True
                print(f"Game over! ({start_row}, {start_col})")
                break
        else:
            start_col += 1


if not moving_commands and not game_over and not all_coals_are_collected:
    print(f"{all_coals - coals_collected} coals left. ({start_row}, {start_col})")