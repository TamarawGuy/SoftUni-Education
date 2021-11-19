def read_matrix():
    size = int(input())
    matrix = []
    for _ in range(size):
        line = [int(x) for x in input().split(" ")]
        matrix.append(line)

    return matrix


def get_first_diagonal_sum(matrix):
    size = len(matrix)
    the_sum = 0
    for i in range(size):
        the_sum += matrix[i][i]
    
    return the_sum
    

def get_second_diagonal_sum(matrix):
    size = len(matrix)
    the_sum = 0
    for i in range(size):
        the_sum += matrix[i][size-1]
        size -= 1
    
    return the_sum


matrix = read_matrix()
print(get_first_diagonal_sum(matrix))
print(get_second_diagonal_sum(matrix))
