product = input()
day = input()
quantity = int(input())

work_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']
result = 0

if day in work_day:
    if product == "banana":
        result = 2.5 * quantity
    elif product == "apple":
        result = 1.20 * quantity
    elif product == "orange":
        result = 0.85 * quantity
    elif product == "grapefruit":
        result = 1.45 * quantity
    elif product == "kiwi":
        result = 2.70 * quantity
    elif product == "pineapple":
        result = 5.5 * quantity
    elif product == "grapes":
        result = 3.85 * quantity

elif day in weekend:
    if product == "banana":
        result = 2.7 * quantity
    elif product == "apple":
        result = 1.25 * quantity
    elif product == "orange":
        result = 0.9 * quantity
    elif product == "grapefruit":
        result = 1.60 * quantity
    elif product == "kiwi":
        result = 3 * quantity
    elif product == "pineapple":
        result = 5.6 * quantity
    elif product == "grapes":
        result = 4.2 * quantity
    
print(f"{result:.2f}"")