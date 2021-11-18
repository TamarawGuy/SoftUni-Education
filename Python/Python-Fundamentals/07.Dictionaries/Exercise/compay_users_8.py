d = {}

while True:
    line = input().split(" -> ")
    if line[0] == 'End':
        break

    company_name = line[0]
    id = line[1]

    if company_name not in d:
        d[company_name] = []
        d[company_name].append(id)
    else:
        if id not in d[company_name]:
            d[company_name].append(id)

sorted_d = dict(sorted(d.items(), key=lambda x: x[0]))
for key, value in sorted_d.items():
    print(f"{key}")
    for item in value:
        print(f"-- {item}")