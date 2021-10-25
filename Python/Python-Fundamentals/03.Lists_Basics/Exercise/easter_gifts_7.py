line = input().split(" ")

while True:
    command = input().split(" ")
    if command[0] == "No":
        break
    if command[0] == "OutOfStock":
        gift = command[1]
        for i in range(len(line)):
            if line[i] == gift:
                line[i] = "None"
            
    elif command[0] == 'Required':
        gift = command[1]
        index = int(command[2])
        if index < len(line):
            line[index] = gift
    
    elif command[0] == 'JustInCase':
        gift = command[1]
        line[-1] = gift

for item in line:
    if item != "None":
        print(item, end=" ")