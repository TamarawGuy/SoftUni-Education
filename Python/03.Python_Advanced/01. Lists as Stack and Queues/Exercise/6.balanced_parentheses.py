def check_if_parenthese_balanced(my_str):
    stack = []
    brackets = {
        '(': ")",
        '[': ']',
        '{': '}',
    }

    is_valid = True

    for i in range(len(my_str)):
        char = my_str[i]
        if char in brackets.keys():
            stack.append(char)
        else:
            if stack:
                last_piece = stack.pop()
                if char != brackets[last_piece]:
                    is_valid = False
                    return "NO"
                else:
                    is_valid = True
            else:
                return "NO"

    if is_valid and not stack:
        return "YES"
    else:
        return "NO"


s = input()
print(check_if_parenthese_balanced(s))