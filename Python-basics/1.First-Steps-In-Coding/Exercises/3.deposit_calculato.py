deposit_sum = float(input())
months = int(input())
annual_interest_percent = float(input())

annual_interest = deposit_sum * annual_interest_percent / 100
annual_interest_1_month = annual_interest / 12
total_sum = deposit_sum + annual_interest_1_month * months
print(total_sum)