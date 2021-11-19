#####################
##### First way #####
#####################


def filter_input(line):
    matrix_of_lists_of_str = [
        [el for el in list_as_str.split()]
        for list_as_str in line.split("|")[::-1]
    ]

    return matrix_of_lists_of_str


def make_int_matrix(matrix):
    int_matrix = [
        [int(x) for x in row]
        for row in matrix
    ]

    return int_matrix


def make_matrix_flat(matrix):
    return [x for sublist in matrix for x in sublist]


def print_result(flat_matrix):
    print(*flat_matrix)
    

my_str = input()
matrix_str = filter_input(my_str)
matrix_int = make_int_matrix(matrix_str)
flat_matrix = make_matrix_flat(matrix_int)
print_result(flat_matrix)


######################
##### Second way #####
######################

result = [
    [int(el) for el in list_as_str.split()]
    for list_as_str in input().split("|")[::-1]
]

result_int_list = [x for sublist in result for x in sublist]
print(*result_int_list)

