line = input().split(", ")

valid_usernames = []

for name in line:
    if 3 <= len(name) <= 16:
        list_name = list(name)
        is_valid = False
    else:
        continue

    for ch in list_name:
        if ch.isalpha() or ch.isdigit() or ch == '-' or ch == '_':
            is_valid = True
        else:
            is_valid = False
            break
    
    if is_valid:
        valid_usernames.append(name)
    
for item in valid_usernames:
    print(item)