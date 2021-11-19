n = int(input())
stack = []

for _ in range(n):
    command = input().split()

    if command[0] == '1':
        x = int(command[1])
        stack.append(x)

    elif command[0] == '2':
        if stack:
            del stack[-1]

    elif command[0] == '3':
        if stack:
            print(max(stack))

    elif command[0] == '4':
        if stack:
            print(min(stack))
    
print(", ".join(map(str, stack[::-1])))