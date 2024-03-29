def strs_to_ints(strs):
    return [int(x) for x in strs]


def read_matrix():
    rows = int(input())
    return [strs_to_ints(input().split(", ")) for _ in range(rows)]


def get_even_matrix(matrix):
    return [[x for x in row if x % 2 == 0] for row in matrix]


def print_result(matrix):
    print(matrix)


matrix = read_matrix()
even_matrix = get_even_matrix(matrix)
print_result(even_matrix)
