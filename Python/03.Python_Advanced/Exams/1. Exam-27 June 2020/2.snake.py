def read_matrix():
    matrix = []

    for _ in range(size):
        line = list(input())
        matrix.append(line)
    
    return matrix


def find_snake_coordinates(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'S':
                return r, c


def count_food_in_game(matrix):
    food_count = 0

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == '*':
                food_count += 1


def check_if_there_are_burrows(matrix):
    for r1 in range(size):
        for c1 in range(size):
            if matrix[r1][c1] == "B":
                return True
            
    return False


def check_if_coordinates_are_valid(r, c):
    return 0 <= r < size and 0 <= c < size


def find_burrow_positions(matrix):
    l = []

    for r1 in range(size):
        for c1 in range(size):
            if matrix[r1][c1] == "B":
                coordinates = (r1, c1)
                l.append(coordinates)

    return l


def print_matrix_result(matrix):
    for row in matrix:
        print("".join(row))


size = int(input())
m = read_matrix()
start_row, start_col = find_snake_coordinates(m)
eaten_food = 0
out_of_territory = False

if check_if_there_are_burrows(m):
    
    first_burrow, second_burrow = find_burrow_positions(m)

    while not out_of_territory and eaten_food != 10:
        command = input()

        if command == "up":
            start_row -= 1

            if check_if_coordinates_are_valid(start_row, start_col):
                m[start_row+1][start_col] = "."
                
                if m[start_row][start_col] == "*":
                    m[start_row][start_col] = "S"
                    eaten_food += 1

                elif m[start_row][start_col] == "B":
                    if start_row == first_burrow[0] and start_col == first_burrow[1]:
                        m[start_row][start_col] = "."
                        start_row, start_col = second_burrow[0], second_burrow[1]
                        m[start_row][start_col] = "S"
                    
                    elif start_row == second_burrow[0] and start_col == second_burrow[1]:
                        m[start_row][start_col] = "."
                        start_row, start_col = first_burrow[0], first_burrow[1]
                        m[start_row][start_col] = "S"
                
                else:
                    m[start_row][start_col] = "S"
            
            else:
                m[start_row+1][start_col] = "."
                out_of_territory = True

        elif command == 'right':
            start_col += 1

            if check_if_coordinates_are_valid(start_row, start_col):
                m[start_row][start_col-1] = "."
                
                if m[start_row][start_col] == "*":
                    m[start_row][start_col] = "S"
                    eaten_food += 1

                elif m[start_row][start_col] == "B":
                    if start_row == first_burrow[0] and start_col == first_burrow[1]:
                        m[start_row][start_col] = "."
                        start_row, start_col = second_burrow[0], second_burrow[1]
                        m[start_row][start_col] = "S"
                    
                    elif start_row == second_burrow[0] and start_col == second_burrow[1]:
                        m[start_row][start_col] = "."
                        start_row, start_col = first_burrow[0], first_burrow[1]
                        m[start_row][start_col] = "S"
                
                else:
                    m[start_row][start_col] = "S"
            
            else:
                m[start_row][start_col-1] = "."
                out_of_territory = True

        elif command == 'down':
            start_row += 1

            if check_if_coordinates_are_valid(start_row, start_col):
                m[start_row-1][start_col] = "."
                
                if m[start_row][start_col] == "*":
                    m[start_row][start_col] = "S"
                    eaten_food += 1

                elif m[start_row][start_col] == "B":
                    if start_row == first_burrow[0] and start_col == first_burrow[1]:
                        m[start_row][start_col] = "."
                        start_row, start_col = second_burrow[0], second_burrow[1]
                        m[start_row][start_col] = "S"
                    
                    elif start_row == second_burrow[0] and start_col == second_burrow[1]:
                        m[start_row][start_col] = "."
                        start_row, start_col = first_burrow[0], first_burrow[1]
                        m[start_row][start_col] = "S"
                
                else:
                    m[start_row][start_col] = "S"
            
            else:
                m[start_row-1][start_col] = "."
                out_of_territory = True

        elif command == 'left':
            start_col -= 1

            if check_if_coordinates_are_valid(start_row, start_col):
                m[start_row][start_col+1] = "."
                
                if m[start_row][start_col] == "*":
                    m[start_row][start_col] = "S"
                    eaten_food += 1

                elif m[start_row][start_col] == "B":
                    if start_row == first_burrow[0] and start_col == first_burrow[1]:
                        m[start_row][start_col] = "."
                        start_row, start_col = second_burrow[0], second_burrow[1]
                        m[start_row][start_col] = "S"
                    
                    elif start_row == second_burrow[0] and start_col == second_burrow[1]:
                        m[start_row][start_col] = "."
                        start_row, start_col = first_burrow[0], first_burrow[1]
                        m[start_row][start_col] = "S"
                
                else:
                    m[start_row][start_col] = "S"
            
            else:
                m[start_row][start_col+1] = "."
                out_of_territory = True

else:
    while not out_of_territory and eaten_food != 10:
        command = input()

        if command == "up":
            start_row -= 1

            if check_if_coordinates_are_valid(start_row, start_col):
                m[start_row+1][start_col] = "."
                
                if m[start_row][start_col] == "*":
                    m[start_row][start_col] = "S"
                    eaten_food += 1

                else:
                    m[start_row][start_col] = "S"
            
            else:
                m[start_row+1][start_col] = "."
                out_of_territory = True
        
        elif command == 'right':
            start_col += 1

            if check_if_coordinates_are_valid(start_row, start_col):
                m[start_row][start_col-1] = "."
                
                if m[start_row][start_col] == "*":
                    m[start_row][start_col] = "S"
                    eaten_food += 1

                else:
                    m[start_row][start_col] = "S"
            
            else:
                m[start_row][start_col-1] = "."
                out_of_territory = True
        
        elif command == 'down':
            start_row += 1

            if check_if_coordinates_are_valid(start_row, start_col):
                m[start_row-1][start_col] = "."
                
                if m[start_row][start_col] == "*":
                    m[start_row][start_col] = "S"
                    eaten_food += 1

                else:
                    m[start_row][start_col] = "S"
            
            else:
                m[start_row-1][start_col] = "."
                out_of_territory = True
            
        elif command == 'left':
            start_col -= 1

            if check_if_coordinates_are_valid(start_row, start_col):
                m[start_row][start_col+1] = "."
                
                if m[start_row][start_col] == "*":
                    m[start_row][start_col] = "S"
                    eaten_food += 1

                else:
                    m[start_row][start_col] = "S"
            
            else:
                m[start_row][start_col+1] = "."
                out_of_territory = True


if out_of_territory:
    print("Game over!")
    print(f"Food eaten: {eaten_food}")
    print_matrix_result(m)

elif eaten_food == 10:
    print(f"You won! You fed the snake.")
    print(f"Food eaten: {eaten_food}")
    print_matrix_result(m)