done = False
d_items = {'shards': 0, 'fragments': 0, "motes": 0}
d_junk = {}

while done == False:
    line = [x.lower() for x in input().split(" ")]

    for i in range(0, len(line), 2):
        item = line[i+1]
        number = int(line[i])

        if item in d_items:
            d_items[item] += number

        if item not in d_items:
            if item in d_junk:
                d_junk[item] += number
            else:
                d_junk[item] = number
            continue
            
        if d_items[item] >= 250:
            d_items[item] -= 250
            done = True
            break

sorted_items = dict(sorted(d_items.items(), key = lambda x: (-x[1], x[0])))
sorted_junk = dict(sorted(d_junk.items(), key=lambda x: x[0]))

if item == 'shards':
    print("Shadowmourne obtained!")
    for key, value in sorted_items.items():
        print(f"{key}: {value}")
    
    for key, value in sorted_junk.items():
        print(f"{key}: {value}")
    
elif item == 'fragments':
    print("Valanyr obtained!")
    for key, value in sorted_items.items():
        print(f"{key}: {value}")
    
    for key, value in sorted_junk.items():
        print(f"{key}: {value}")

elif item == 'motes':
    print("Dragonwrath obtained!")
    for key, value in sorted_items.items():
        print(f"{key}: {value}")
    
    for key, value in sorted_junk.items():
        print(f"{key}: {value}")