n = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

sum = 0
helmet_broken = 0
sword_broken = 0
shield_broken = 0
armor_broken = 0

for i in range(1, n+1):
    if i % 2 == 0:
        helmet_broken += 1
    if i % 3 == 0:
        sword_broken += 1
    if i % 2 == 0 and i % 3 == 0:
        shield_broken += 1
        if shield_broken % 2 == 0:
            armor_broken += 1
        
sum = helmet_broken * helmet_price + sword_broken * sword_price + shield_broken * shield_price + armor_broken * armor_price

    
        
    
print(f"Gladiator expenses: {sum:.2f} aureus")