def read_matrix():
    matrix = []

    for i in range(8):
        line = list(input())
        line = [x for x in line if x != " "]
        matrix.append(line)

    return matrix

def check_if_coordinates_are_valid(r, c):
    return 0 <= r < 8 and 0 <= c < 8


def check_if_queen_captures_king(matrix, r, c):

    for i in range(1, 8):
    
        if not check_if_coordinates_are_valid(r-i, c):
            break
        else:
            if matrix[r-i][c] == "K":
                return True
            
            elif matrix[r-i][c] == "Q":
                break

    for i in range(1, 8):
    
        if not check_if_coordinates_are_valid(r-i, c-i):
            break
        else:
            if matrix[r-i][c-i] == "K":
                return True
            
            elif matrix[r-i][c-i] == "Q":
                break

    for i in range(1, 8):
    
        if not check_if_coordinates_are_valid(r-i, c+i):
            break
        else:
            if matrix[r-i][c+i] == "K":
                return True

            elif matrix[r-i][c+i] == "Q":
                break

    for i in range(1, 8):
    
        if not check_if_coordinates_are_valid(r, c+i):
            break
        else:
            if matrix[r][c+i] == "K":
                return True

            elif matrix[r][c+i] == "Q":
                break

    for i in range(1, 8):
    
        if not check_if_coordinates_are_valid(r+i, c+i):
            break
        else:
            if matrix[r+i][c+i] == "K":
                return True
            
            elif matrix[r+i][c+i] == "Q":
                break


    for i in range(1, 8):
    
        if not check_if_coordinates_are_valid(r+i, c):
            break
        else:
            if matrix[r+i][c] == "K":
                return True
            
            elif matrix[r+i][c] == 'Q':
                break

    for i in range(1, 8):
    
        if not check_if_coordinates_are_valid(r+i, c-i):
            break
        else:
            if matrix[r+i][c-i] == "K":
                return True
            
            elif matrix[r+i][c-i] == 'Q':
                break

    for i in range(1, 8):

        if not check_if_coordinates_are_valid(r, c-i):
            break
        else:
            if matrix[r][c-i] == "K":
                return True

            elif matrix[r][c-i] == "Q":
                break

    return False


m = read_matrix()
d = {}
for row in range(8):
    for col in range(8):
        if m[row][col] == "Q":
            if check_if_queen_captures_king(m, row, col):
                d[row] = col


if d:
    for key, value in d.items():
        print(f"[{key}, {value}]")

if not d:
    print("The king is safe!")