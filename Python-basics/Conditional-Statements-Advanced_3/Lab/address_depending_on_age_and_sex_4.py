age = int(input())
sex = input()

if sex == 'f':
    if age < 16:
        print("Miss.")
    elif age >= 16:
        print("Ms.")

elif sex == 'm':
    if age < 16:
        print("Master")
    elif age >= 16:
        print("Mr.")