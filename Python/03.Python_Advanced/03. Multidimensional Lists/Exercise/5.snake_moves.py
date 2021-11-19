def make_matrix():
    row, col = [int(x) for x in input().split(" ")]
    matrix = []

    for r in range(row):
        line = [0] * col
        matrix.append(line)
    
    return matrix


def fill_up_matrix(matrix, word):
    word_index = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            matrix[r][c] = word[word_index]
            word_index += 1
            if word_index == len(word):
                word_index = 0
        
    return matrix


def print_result(matrix):
    for row_index in range(len(matrix)):
        row = matrix[row_index]
        if row_index % 2 == 1:
            row.reverse()
            print("".join(row))
        else:
            print("".join(row))


m = make_matrix()
word = input()
matrix = fill_up_matrix(m, word)
print_result(matrix)






'''
row, col = [int(x) for x in input().split(" ")]

word = input()
matrix = []

for row_index in range(row):
    matrix.append([0 for el in range(col)])

index_word = 0

for row_index in range(row):
    for col_index in range(col):
        matrix[row_index][col_index] = word[index_word]
        index_word += 1
        if index_word == len(word):
            index_word = 0

for row_index in range(row):
    if row_index % 2 == 1:
        matrix[row_index].reverse()
    print("".join(matrix[row_index]))

'''