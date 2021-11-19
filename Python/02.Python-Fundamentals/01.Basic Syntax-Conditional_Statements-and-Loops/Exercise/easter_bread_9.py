budget = float(input())
price_per_1_kg_flour = float(input())

eggs = 0
cozonacs = 0

pack_eggs = 0.75 * price_per_1_kg_flour
milk_250 = (1.25 * price_per_1_kg_flour) / 4

total_price_1_cozonac = price_per_1_kg_flour + pack_eggs + milk_250

while budget - total_price_1_cozonac > 0:
    budget -= total_price_1_cozonac
    eggs += 3
    cozonacs += 1
    if cozonacs % 3 == 0:
        eggs -= cozonacs - 2
    
print(f"You made {cozonacs} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.")