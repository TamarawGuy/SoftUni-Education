def solve(line):
    result = {ch: ord(ch) for ch in line}
    return result

chars = input().split(", ")
print(solve(chars))