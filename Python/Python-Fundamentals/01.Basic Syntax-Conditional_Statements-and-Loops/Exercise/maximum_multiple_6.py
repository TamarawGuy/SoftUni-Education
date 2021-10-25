number = int(input())
number += 1
while True:
    year = str(number)
    if len(set(year)) == len(year):
        print(year)
        break
    number += 1