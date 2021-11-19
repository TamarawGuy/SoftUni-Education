size = int(input())
number_of_bombs = int(input())

def make_matrix_of_zeros():
    matrix = [
        [0] * size
        for _ in range(size)
    ]

    return matrix


def check_if_coordinates_are_valid(row, col):
    return 0 <= row < size and 0 <= col < size


def calculate_numbers_in_cells(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            
            if matrix[r][c] == "*":
                continue
        
            if matrix[r][c] >= 0:
                matrix[r][c] = 0

                if check_if_coordinates_are_valid(r + 1, c):
                    
                    if matrix[r+1][c] == "*":
                        matrix[r][c] += 1

                if check_if_coordinates_are_valid(r - 1, c):
                    if matrix[r-1][c] == "*":
                        matrix[r][c] += 1

                if check_if_coordinates_are_valid(r, c + 1):
                    if matrix[r][c+1] == "*":
                        matrix[r][c] += 1

                if check_if_coordinates_are_valid(r, c - 1):
                    if matrix[r][c-1] == "*":
                        matrix[r][c] += 1
                
                if check_if_coordinates_are_valid(r - 1, c - 1):
                    if matrix[r-1][c-1] == "*":
                        matrix[r][c] += 1
                
                if check_if_coordinates_are_valid(r - 1, c + 1):
                    if matrix[r-1][c+1] == "*":
                        matrix[r][c] += 1
                
                if check_if_coordinates_are_valid(r + 1, c - 1):
                    if matrix[r+1][c-1] == "*":
                        matrix[r][c] += 1
                
                if check_if_coordinates_are_valid(r + 1, c + 1):
                    if matrix[r+1][c+1] == "*":
                        matrix[r][c] += 1


m = make_matrix_of_zeros()

for _ in range(number_of_bombs):
    bomb_coordinates = input()
    bomb_coordinates = bomb_coordinates[1:-1]
    bomb_row, bomb_col = [int(x) for x in bomb_coordinates.split(", ")]
    
    m[bomb_row][bomb_col] = "*"

    calculate_numbers_in_cells(m)

for row in m:
    print(*row)
