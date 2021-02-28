number = int(input())
bonus_point = 0

if number <= 100:
    bonus_point += 5

elif 100 < number < 1000:
    bonus_point += 0.2 * number

else:
    bonus_point += 0.1 * number


if number % 2 == 0:
    bonus_point += 1

if number % 10 == 5:
    bonus_point += 2


print(bonus_point)
print(number + bonus_point)