def print_result(items, avg, d):
    print(f"Count of items: {items}")
    print(f"Average quality: {avg:.2f}")
    for k, v in d.items():
        print(f"{k} -> {', '.join(v)}")


def filter_information(l):
    category = line[0]
    item = line[1]
    quantity_quality = line[2].split(";")
    quantity = int(quantity_quality[0].split(":")[1])
    quality = int(quantity_quality[1].split(":")[1])

    return category, item, quantity, quality


categories = input().split(", ")
n = int(input())
total_items = 0
total_quality = 0
d_categories_items = {x: [] for x in categories}


for _ in range(n):
    line = input().split(" - ")
    filtered_info = filter_information(line)

    category = filtered_info[0]
    item = filtered_info[1]
    quantity = filtered_info[2]
    quality = filtered_info[3]

    total_items += quantity
    total_quality += quality
    average_quality = total_quality / len(categories)
    d_categories_items[category].append(item)


print_result(total_items, average_quality, d_categories_items)