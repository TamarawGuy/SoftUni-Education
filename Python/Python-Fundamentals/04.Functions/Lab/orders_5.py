name = input()
q = int(input())

def solve(product, quantity):
    if product == "coffee":
        res = 1.50 * quantity
    elif product == "water":
        res = 1.00 * quantity
    elif product == "coke":
        res = 1.40 * quantity
    elif product == "snacks":
        res = 2.00 * quantity
    return f"{res:.2f}"

print(solve(name, q))