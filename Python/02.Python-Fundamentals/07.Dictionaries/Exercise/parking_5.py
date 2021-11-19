d = {}

n = int(input())

for i in range(n):
    command = input().split(" ")

    if command[0] == 'register':
        username = command[1]
        plate_number = command[2]

        if username in d:
            print(f"ERROR: already registered with plate number {plate_number}")
        else:
            d[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
    
    elif command[0] == 'unregister':
        username = command[1]

        if username not in d:
            print(f"ERROR: user {username} not found")
        else:
            del d[username]
            print(f"{username} unregistered successfully")
        
for key, value in d.items():
    print(f"{key} => {value}")