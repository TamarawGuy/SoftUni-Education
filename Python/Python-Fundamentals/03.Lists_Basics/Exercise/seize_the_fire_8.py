line = input().split("#")
water = int(input())
effort = 0
total_fire = 0
valid_amounts = []
for item in line:
    tokens = item.split(" = ")
    type_of_fire = tokens[0]
    amount = int(tokens[1])

    if type_of_fire == "Low" and amount >= 1 and amount <= 50:
        if water - amount >= 0:
            water -= amount
            effort += 0.25*amount
            total_fire += amount
            valid_amounts.append(amount)
    
    if type_of_fire == "Medium" and amount >= 51 and amount <= 80:
        if water - amount >= 0:
            water -= amount
            effort += 0.25*amount
            total_fire += amount
            valid_amounts.append(amount)
    
    if type_of_fire == "High" and amount >= 81 and amount <= 125:
        if water - amount >= 0:
            water -= amount
            effort += 0.25*amount
            total_fire += amount
            valid_amounts.append(amount)

print("Cells:")
for smth in valid_amounts:
    print(f" - {smth}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")