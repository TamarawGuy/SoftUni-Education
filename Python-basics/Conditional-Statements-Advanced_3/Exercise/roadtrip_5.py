budget = float(input())
season = input()
destination = ""
place = ""

if budget <= 100:
    destination = "Bulgaria"
elif 100 < budget <= 1000:
    destination = "Balkans"
elif budget > 1000:
    destination = "Europe"

if destination == "Bulgaria":
    if season == "summer":
        price = 0.3 * budget
        place = 'Camp'
    elif season == 'winter':
        place = "Hotel"
        price = 0.7 * budget

elif destination == "Balkans":
    if season == "summer":
        place = 'Camp'
        price = 0.4 * budget
    elif season == 'winter':
        place = "Hotel"
        price = 0.8 * budget

elif destination == "Europe":
    if season == "summer":
        place = 'Camp'
        price = 0.9 * budget
    elif season == 'winter':
        place = "Hotel"
        price = 0.9 * budget


print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")