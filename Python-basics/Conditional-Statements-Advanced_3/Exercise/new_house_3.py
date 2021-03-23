flower = input()
number_of_flowers = int(input())
budget = int(input())

if flower == "Roses":
    final_price = number_of_flowers * 5
    if number_of_flowers > 80:
        final_price -= final_price * 0.1

elif flower == "Dahlias":
    final_price = number_of_flowers * 3.8
    if number_of_flowers > 90:
        final_price -= final_price * 0.15
    
elif flower == "Tulips":
    final_price = number_of_flowers * 2.8
    if number_of_flowers > 80:
        final_price -= final_price * 0.15
    
elif flower == "Narcissus":
    final_price = number_of_flowers * 3
    if number_of_flowers < 120:
        final_price += final_price * 0.15

elif flower == "Gladiolus":
    final_price = number_of_flowers * 2.5
    if number_of_flowers < 80:
        final_price += final_price * 0.2
    
if final_price >= budget:
    print(f"Hey, you have a great garden weith {number_of_flowers} {flower} and {final_price-budget:.2f} leva left.")
else:
    print(f"Not enough money, you need {budget-final_price:.2f} leva more.")