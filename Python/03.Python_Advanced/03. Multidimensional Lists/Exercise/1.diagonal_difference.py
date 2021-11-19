def read_matrix():
    size = int(input())
    matrix = []
    for _ in range(size):
        line = [int(x) for x in input().split(" ")]
        matrix.append(line)
    
    return matrix

def get_first_diagonal_sum(matrix):
    the_sum = 0
    for i in range(len(matrix)):
        the_sum += matrix[i][i]
    
    return the_sum


def get_second_diagonal_sum(matrix):
    the_sum = 0
    size = len(matrix)
    for r in range(size):
        the_sum += matrix[r][size-1]
        size -= 1

    return the_sum


def get_diagonal_difference(d1, d2):
    return abs(d1-d2)


matrix = read_matrix()
s1 = get_first_diagonal_sum(matrix)
s2 = get_second_diagonal_sum(matrix)
print(get_diagonal_difference(s1, s2))
