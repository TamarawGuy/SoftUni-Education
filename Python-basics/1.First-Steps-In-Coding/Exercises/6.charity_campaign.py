days = int(input())
cookers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

price_for_cakes = cakes * 45
price_for_waffles = waffles * 5.8
price_for_pancakes = pancakes * 3.2

total_sum_1_day = (price_for_cakes + price_for_waffles + price_for_pancakes) * cookers
total_sum = total_sum_1_day * days

after_taxes_sum = total_sum - (total_sum * 1 / 8)
print(after_taxes_sum)