##### FIrst way #####

def solve(countries, capitals):
    return list(zip(countries, capitals))


def print_result(result):
    for item in result:
        print(f"{item[0]} -> {item[1]}")


countries = input().split(", ")
capitals = input().split(", ")
print_result(solve(countries, capitals))


##### Second way #####
cities = input().split(", ")
capitals = input().split(", ")
result = {cities[index]: capitals[index] for index in range(len(capitals))}
print(*[f"{key} -> {value}" for key, value in result.items()], sep="\n")