names = input().split(", ")

d_item = {name: [] for name in names}
d_price = {name: 0 for name in names}


while True:
    items = input().split("-")
    if items[0] == 'End':
        break
    
    n = items[0]
    item = items[1]
    pricing = int(items[2])

    if item not in d_item[n]:
        d_item[n].append(item)
        d_price[n] += pricing

for k, v in d_item.items():
    print(f"{k} -> Items: {len(d_item[k])}, Cost: {d_price[k]}")

    