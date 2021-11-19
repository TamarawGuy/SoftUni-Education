def solve(line):
    filtered_line = [word for word in line if len(word) % 2 == 0]
    return "\n".join(filtered_line)


l = input().split(" ")
print(solve(l)))