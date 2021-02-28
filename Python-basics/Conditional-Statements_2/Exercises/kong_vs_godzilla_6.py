film_budget = float(input())
statists = int(input())
price_outfit = float(input())

price_decor = 0.1 * film_budget
price_outfit_team = statists * price_outfit

if statists > 150:
    discount = 0.1 * price_outfit_team
    price_outfit_team -= discount


total_price_for_film = price_decor + price_outfit_team

if total_price_for_film >= film_budget:
    money_left = total_price_for_film - film_budget
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")

else:
    money_needed = film_budget - total_price_for_film
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")