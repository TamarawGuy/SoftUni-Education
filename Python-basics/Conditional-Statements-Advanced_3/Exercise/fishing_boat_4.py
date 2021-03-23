budget = int(input())
season = input()
fishermen = int(input())
price = 0

if season == "Spring":
    if fishermen <= 6:
        price = 3000 - (3000 * 0.1)
    elif fishermen >= 7 and fishermen <= 11:
        price = 3000 - (3000 * 0.15)
    elif fishermen >= 12:
        price = 3000 - (3000 * 0.25)
    
elif season == "Summer" or season == "Autumn":
    if fishermen <= 6:
        price = 4200 - (4200 * 0.1)
    elif fishermen >= 7 and fishermen <= 11:
        price = 4200 - (4200 * 0.15)
    elif fishermen >= 12:
        price = 4200 - (4200 * 0.25)

if season == "Winter":
    if fishermen <= 6:
        price = 2600 - (2600 * 0.1)
    elif fishermen >= 7 and fishermen <= 11:
        price = 2600 - (2600 * 0.15)
    elif fishermen >= 12:
        price = 2600 - (2600 * 0.25)


if fishermen % 2 == 0 and season != "Autumn":
    price -= price * 0.05

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
