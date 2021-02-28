holiday_price = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

total_price_toys = puzzles * 2.6 + dolls * 3 + teddy_bears * 4.1 + minions * 8.2 + trucks * 2
total_toys = puzzles + dolls + teddy_bears + minions + trucks

if total_toys >= 50:
    discount = 0.25 * total_price_toys
    total_price_toys -= discount
    rent_to_pay = 0.1 * total_price_toys
    final_profit = total_price_toys - rent_to_pay

else:
    rent_to_pay = 0.1 * total_price_toys
    final_profit = total_price_toys - rent_to_pay


if final_profit >= holiday_price:
    money_left = final_profit - holiday_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = holiday_price - final_profit
    print(f"Not enough money! {money_needed:.2f} lv needed.")