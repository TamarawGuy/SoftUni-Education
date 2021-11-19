def read_matrix():
    row, col = [int(x) for x in input().split(" ")]
    matrix = []
    for _ in range(row):
        line = [int(x) for x in input().split(" ")]
        matrix.append(line)
    
    return matrix


def get_squares_from_matrix(matrix):
    squares = []
    for r in range(len(matrix)-2):
        for c in range(len(matrix[r])-2):
            square = [
                [matrix[r][c], matrix[r][c+1], matrix[r][c+2]],
                [matrix[r+1][c], matrix[r+1][c+1], matrix[r+1][c+2]],
                [matrix[r+2][c], matrix[r+2][c+1], matrix[r+2][c+2]],
            ]
            squares.append(square)
    
    return squares


def max_sum_and_matrix(matrices):
    max_sum = 0
    max_matrix = None
    for matrix in matrices:
        the_sum = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                the_sum += matrix[r][c]
        
        if max_sum < the_sum:
            max_sum = the_sum
            max_matrix = matrix
        
    return max_sum, max_matrix


matrix = read_matrix()
many_matrices = get_squares_from_matrix(matrix)
s, m = max_sum_and_matrix(many_matrices)
print(f"Sum = {s}")
for row in m:
    print(" ".join(map(str, row)))
