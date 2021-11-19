d = {}

while True:
    command = input()
    if command == 'stop':
        break

    number = int(input())

    if command not in d:
        d[command] = number
    else:
        d[command] += number
    
for key, value in d.items():
    print(f"{key} -> {value}")