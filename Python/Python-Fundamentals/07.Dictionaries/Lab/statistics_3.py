d = {}
products = 0
total_quantity = 0

while True:
    commmand = input()
    if commmand == 'statistics':
        break

    tokens = commmand.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])

    if product in d:
        d[product] += quantity
        total_quantity += quantity
    else:
        d[product] = quantity
        products += 1
        total_quantity += quantity
    
print("Products in stock:")
for key, value in d.items():
    print(f"- {key}: {value}")

print(f"Total Products: {products}")
print(f"Total Quantity: {total_quantity}")