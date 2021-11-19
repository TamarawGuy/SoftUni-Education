def read_matrix():
    row, col = [int(x) for x in input().split(" ")]
    matrix = []
    for _ in range(row):
        line = input().split(" ")
        matrix.append(line)
    
    return matrix


def check_if_coordinates_are_valid(matrix, r1, c1, r2, c2):
    is_valid = True

    if r1 < 0 or r1 >= len(matrix):
        is_valid = False
    elif r2 < 0 or r2 >= len(matrix):
        is_valid = False
    elif c1 < 0 or c1 > len(matrix[0]):
        is_valid = False
    elif c2 < 0 or c2 > len(matrix[0]):
        is_valid = False
    
    return is_valid


def swap_matrix(matrix, r1, c1, r2, c2):
    matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
    return matrix

matrix = read_matrix()

while True:
    command = input().split(" ")
    if command[0] == 'END':
        break
    
    elif command[0] == 'swap':
        if len(command[1:]) == 4:
            row1 = int(command[1])
            row2 = int(command[2])
            col1 = int(command[3])
            col2 = int(command[4])

            if check_if_coordinates_are_valid(matrix, row1, row2, col1, col2):
                new_matrix = swap_matrix(matrix, row1, row2, col1, col2)
                for row in new_matrix:
                    print(" ".join(map(str, row)))
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
