def read_matrix():
    row, col = [int(x) for x in input().split(", ")]
    matrix = []
    for _ in range(row):
        line = [int(x) for x in input().split(" ")]
        matrix.append(line)

    return matrix


def get_sum_of_each_column(matrix):
    the_sum = 0
    rows = len(matrix)
    cols = len(matrix[0])
    list_of_sums = []
    for c in range(cols):
        for r in range(rows):
            the_sum += matrix[r][c]
        list_of_sums.append(the_sum)
        the_sum = 0

    return list_of_sums

def print_result(res):
    for item in res:
        print(item)


matrix = read_matrix()
sums = get_sum_of_each_column(matrix)
print_result(sums)

























'''
def read_matrix():
    row, col = [int(x) for x in input().split(", ")]
    matrix = []
    for _ in range(row):
        line = [int(x) for x in input().split(" ")]
        matrix.append(line)

    return matrix


def get_sum_of_columns(matrix):
    the_sum = 0
    row_index = len(matrix)
    col_index = len(matrix[0])
    l = []
    for c in range(col_index):
        for r in range(row_index):
            the_sum += matrix[r][c]
        l.append(the_sum)
        the_sum = 0
    
    return "\n".join(map(str, l))

matrix = read_matrix()
print(get_sum_of_columns(matrix))

'''