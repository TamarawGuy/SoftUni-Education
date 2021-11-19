def read_matrix():
    matrix = [
        [int(x) for x in input().split(", ")]
        for _ in range(n)
    ]

    return matrix


def get_first_diagonal(matrix):
    return [matrix[i][i] for i in range(len(matrix))]


def get_second_diagonal(matrix):
    return [matrix[i-1][len(matrix)-i] for i in range(1, len(matrix)+1)]


def print_result(res1, res2):
    print(f"First diagonal: {', '.join(map(str, res1))}. Sum: {sum(res1)}")
    print(f"Second diagonal: {', '.join(map(str, res2))}. Sum: {sum(res2)}")


n = int(input())
matrix = read_matrix()
first_diagonal = get_first_diagonal(matrix)
second_diagonal = get_second_diagonal(matrix)
print_result(first_diagonal, second_diagonal)