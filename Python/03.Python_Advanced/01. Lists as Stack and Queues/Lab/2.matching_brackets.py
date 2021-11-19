def match_bracket(my_str):
    s = []
    res = []
    for i in range(len(my_str)):
        char = my_str[i]
        if char == '(':
            s.append(i)
        elif char == ')':
            start_index = s.pop()
            res.append(my_str[start_index:i+1])

    return res


def print_result(result):
    for item in result:
        print(item)

s = input()
subexpressions = match_bracket(s)
print_result(subexpressions)