##### First way #####


def read_rows_cols():
    r, c = [int(x) for x in input().split(" ")]
    return r, c


def make_palindrome_matrix(rows, cols):
    mat = []
    for number in range(97, 97+rows):
        l = []
        res = ''
        for nested_number in range(number, number+cols):
            res += f"{chr(number)}{chr(nested_number)}{chr(number)} "
        l.append(res)
        mat.append(l)
        
    return mat

def print_result(res):
    for item in res:
        print("\n".join(item))


rows, cols = read_rows_cols()
matrix = make_palindrome_matrix(rows, cols)
print_result(matrix)


##### Second way #####


rows, cols = [int(x) for x in input().split(" ")]
result = [
    [f"{chr(number)}{chr(nested_num)}{chr(number)} " for nested_num in range(number, number+cols)]
    for number in range(97, 97+rows)
]

print("\n".join([" ".join(row) for row in result]))



##### Third way #####


r, c = [int(x) for x in input().split(" ")]
for number in range(97, 97+r):
    res = ""
    for nested_number in range(number, number+c):
        res += f"{chr(number)}{chr(nested_number)}{chr(number)} "
    
    print(res)

'''