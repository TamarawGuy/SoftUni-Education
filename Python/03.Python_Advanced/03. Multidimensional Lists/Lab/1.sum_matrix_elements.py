def read_matrix():
    matrix = []
    rows, cols = [int(x) for x in input().split(", ")]

    for _ in range(rows):
        line = [int(x) for x in input().split(", ")]
        matrix.append(line)
    
    return matrix


def get_sum_of_matrix(matrix):
    the_sum = 0

    for r in range(len(matrix)):
        row = matrix[r]
        for c in range(len(row)):
            the_sum += matrix[r][c]
        
    return the_sum


def print_result(s, m):
    print(s)
    print(m)


matrix = read_matrix()
my_sum = get_sum_of_matrix(matrix)
print_result(my_sum, matrix)




'''

def read_matrix():
    row, col = [int(x) for x in input().split(", ")]
    matrix = []
    for _ in range(row):
        line = [int(x) for x in input().split(", ")]
        matrix.append(line)

    return matrix


def get_sum_of_matrix(matrix):
    the_sum = 0
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            the_sum += matrix[row_index][col_index]
        
    return the_sum

matrix = read_matrix()
print(get_sum_of_matrix(matrix))
print(matrix)

'''