##### First way #####

def solve(line):
    length_line = {word: len(word) for word in line}
    return length_line
    

def print_result(res):
    print(", ".join(['{0} -> {1}'.format(k, v) for k,v in res.items()]))


l = input().split(", ")
print_result(solve(l))


##### Second way #####
names = input().split(", ")
result = [f"{name} -> {len(name)}" for name in names]
print(", ".join(result))


##### Third way - one line code #####
print(", ".join([f"{name} -> {len(name)}" for name in input().split(", ")]))