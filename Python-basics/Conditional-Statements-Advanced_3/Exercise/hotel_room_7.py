month = input()
nights = int(input())

if month == 'May' or month == "October":
    studio_price = nights * 50
    apartment_price = nights * 65

    if 7 < nights <= 14:
        studio_price -= studio_price * 0.05

    elif nights > 14:
        studio_price -= studio_price * 0.3
        apartment_price -= apartment_price * 0.1
    
elif month == 'June' or month == "September":
    studio_price = nights * 75.20
    apartment_price = nights * 68.70

    if nights > 14:
        studio_price -= studio_price * 0.2
        apartment_price -= apartment_price * 0.1

elif month == 'July' or month == "August":
    studio_price = nights * 76
    apartment_price = nights * 77

    if nights > 14:
        apartment_price -= apartment_price * 0.1
    
print(f"Apartment: {apartment_price: .2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")