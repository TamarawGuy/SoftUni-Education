def read_matrix():
    matrix = []
    size = int(input())
    for _ in range(size):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    
    return matrix


def check_if_coordinates_are_valid(matrix, r, c):
    is_valid = True
    
    if r < 0 or r >= len(matrix):
        is_valid = False
    elif c < 0 or c >= len(matrix):
        is_valid = False

    return is_valid


def check_if_line_END(line):
    if len(line) == 1:
        return True
    return False


def filter_info(line):
    r = int(line[1])
    c = int(line[2])
    v = int(line[3])

    return r, c, v


def print_result(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


matrix = read_matrix()

while True:
    line = input().split()
    if check_if_line_END(line):
        break

    if line[0] == "Add":
        info = filter_info(line)
        row, col, value = info

        if check_if_coordinates_are_valid(matrix, row, col):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")

    elif line[0] == 'Subtract':
        info = filter_info(line)
        row, col, value = info

        if check_if_coordinates_are_valid(matrix, row, col):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

    
print_result(matrix)