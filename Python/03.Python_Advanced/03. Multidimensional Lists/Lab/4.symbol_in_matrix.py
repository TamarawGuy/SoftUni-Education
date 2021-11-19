def read_matrix():
    size = int(input())
    matrix = []
    for _ in range(size):
        line = list(input())
        matrix.append(line)

    return matrix


def get_symbol_in_matrix(matrix, symbol):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            current_symbol = matrix[r][c]
            if current_symbol == symbol:
                return r, c


def print_result(my_symbol):
    if my_symbol:
        print(my_symbol)
    else:
        print(f"{symbol} does not occur in the matrix")


matrix = read_matrix()
symbol = input()
my_symbol = get_symbol_in_matrix(matrix, symbol)
print_result(my_symbol)