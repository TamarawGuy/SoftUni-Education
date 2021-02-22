price_strawberries_per_kilo = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())

price_raspberries_per_kilo = price_strawberries_per_kilo / 2
price_oranges_per_kilo = price_raspberries_per_kilo - (price_raspberries_per_kilo * 40 / 100)
price_bananas_per_kilo = price_raspberries_per_kilo - (price_raspberries_per_kilo * 80 / 100)

price_strawberries = strawberries * price_strawberries_per_kilo
price_raspberries = raspberries * price_raspberries_per_kilo
price_oranges = oranges * price_oranges_per_kilo
price_bananas = bananas * price_bananas_per_kilo

total_sum = price_strawberries + price_raspberries + price_oranges + price_bananas
print(total_sum)