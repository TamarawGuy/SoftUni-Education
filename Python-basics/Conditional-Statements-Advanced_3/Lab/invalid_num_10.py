num = int(input())
is_valid = False

if 100 <= num <= 200:
    is_valid = True

if num == 0:
    is_valid = True

if is_valid == False:
    print("invalid")