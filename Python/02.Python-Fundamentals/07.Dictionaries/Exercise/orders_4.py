d_price = {}
d_quantity = {}

while True:
    line = input().split(" ")
    if line[0] == 'buy':
        break

    name = line[0]
    price = float(line[1])
    quantity = int(line[2])

    if name not in d_price:
        d_price[name] = price
        d_quantity[name] = quantity
    elif name in d_price:
        d_quantity[name] += quantity
        if price != d_price[name]:
            d_price[name] = price
        
for key, value in d_price.items():
    print(f"{key} -> {value * d_quantity[key]:.2f}")