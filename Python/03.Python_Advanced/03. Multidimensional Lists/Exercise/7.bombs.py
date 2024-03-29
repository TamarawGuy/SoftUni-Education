def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def explode(row, col, size, matrix):
    bomb = matrix[row][col]

    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if is_valid(r, c, size) and matrix[r][c] > 0:
                matrix[r][c] -= bomb


def print_result(matrix):
    alive_cells = 0
    my_sum = 0

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            number = matrix[row][col]
            if number > 0:
                alive_cells += 1
                my_sum += number

    print(f"Alive cells: {alive_cells}")
    print(f"Sum: {my_sum}")
    for row in matrix:
        print(*row)


n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

bomb_numbers = input().split()

for bomb in bomb_numbers:
    tokens = [int(x) for x in bomb.split(",")]
    bomb_row = tokens[0]
    bomb_col = tokens[1]

    if matrix[bomb_row][bomb_col] > 0:
        explode(bomb_row, bomb_col, n, matrix)
        matrix[bomb_row][bomb_col] = 0


print_result(matrix)