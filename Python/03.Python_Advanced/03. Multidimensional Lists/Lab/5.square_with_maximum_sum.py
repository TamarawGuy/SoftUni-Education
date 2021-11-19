def read_matrix():
    row, col = [int(x) for x in input().split(", ")]
    matrix = []
    for _ in range(row):
        line = [int(x) for x in input().split(", ")]
        matrix.append(line)

    return matrix


def get_squares_from_matrix(matrix):
    squares = []
    for i in range(len(matrix)-1):
        row = matrix[i]
        for j in range(len(row) - 1):
            square = [
                [matrix[i][j], matrix[i][j+1]],
                [matrix[i+1][j], matrix[i+1][j+1]],
            ]
            squares.append(square)
    return squares


def get_max_sum_of_submatrix(matrix, best_sum=0, best_matrix=None):
    submatrices = get_squares_from_matrix(matrix)
    for sub_m in submatrices:
        the_sum = 0
        for row_index in range(len(sub_m)):
            for col_index in range(len(sub_m[row_index])):
                the_sum += sub_m[row_index][col_index]
            
            if best_sum < the_sum:
                best_sum = the_sum
                best_matrix = sub_m
    return best_sum, best_matrix


matrix = read_matrix()
best_sum, best_matrix = get_max_sum_of_submatrix(matrix)

for row in best_matrix:
    print(*row)
print(best_sum)
