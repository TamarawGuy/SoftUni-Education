rent = float(input())

price_for_cake = rent * 20 / 100
price_for_drinks = price_for_cake - (price_for_cake * 45 / 100)
price_for_animator = rent / 3
total_sum = rent + price_for_cake + price_for_drinks + price_for_animator

print(total_sum)


