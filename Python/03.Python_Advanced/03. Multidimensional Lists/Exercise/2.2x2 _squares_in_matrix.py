def read_matrix():
    row, col = [int(x) for x in input().split(" ")]
    matrix = []
    for _ in range(row):
        line = input().split(" ")
        matrix.append(line)
    
    return matrix


def get_squares_from_matrix(matrix):
    squares = []

    for r in range(len(matrix)-1):
        for c in range(len(matrix[r])-1):
            square = [
                [matrix[r][c], matrix[r][c+1]],
                [matrix[r+1][c], matrix[r+1][c+1]]
            ]
            squares.append(square)
    
    return squares

def check_for_squares_with_equal_cells(matrix):
    submatrices = get_squares_from_matrix(matrix)
    same_squares = 0

    for sub_m in submatrices:
        if sub_m[0][0] == sub_m[0][1] == sub_m[1][0] == sub_m[1][1]:
            same_squares += 1
        
    return same_squares


def print_result(res):
    print(res)


m = read_matrix()
result = check_for_squares_with_equal_cells(m)
print_result(result)


























'''

def read_matrix():
    row, col = [int(x) for x in input().split(" ")]
    matrix = []
    for _ in range(row):
        line = input().split(" ")
        matrix.append(line)
    
    return matrix


def get_squares_from_matrix(matrix):
    squares = []
    for row_index in range(len(matrix)-1):
        for col_index in range(len(matrix[row_index])-1):
            square = [
                [matrix[row_index][col_index], matrix[row_index][col_index+1]],
                [matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]],
            ]
            squares.append(square)

    return squares


def count_matrices_with_same_elements(matrices):
    the_count = 0
    for matrix in matrices:
        if matrix[0][0] == matrix[0][1] == matrix[1][0] == matrix[1][1]:
            the_count += 1
        
    return the_count


print(count_matrices_with_same_elements(get_squares_from_matrix(read_matrix())))

'''