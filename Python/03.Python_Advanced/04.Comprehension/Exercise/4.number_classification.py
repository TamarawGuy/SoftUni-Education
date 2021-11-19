def positive_numbers(line):
    return [x for x in line if x >= 0]


def negative_numbers(line):
    return [x for x in line if x < 0]


def even_numbers(line):
    return [x for x in line if x % 2 == 0]


def odd_numbers(line):
    return [x for x in line if x % 2 != 0]


def print_result(l1, l2, l3, l4):
    print(f"Positive: {', '.join(map(str, l1))}")
    print(f"Negative: {', '.join(map(str, l2))}")
    print(f"Even: {', '.join(map(str, l3))}")
    print(f"Odd: {', '.join(map(str, l4))}")


line = [int(x) for x in input().split(", ")]
l1 = positive_numbers(line)
l2 = negative_numbers(line)
l3 = even_numbers(line)
l4 = odd_numbers(line)
print_result(l1, l2, l3, l4)