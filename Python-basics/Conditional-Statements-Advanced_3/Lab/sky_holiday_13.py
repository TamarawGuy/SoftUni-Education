days = int(input())
type_of_room = input()
grade = input()

if type_of_room == 'room for one person':
    if days < 10:
        price = 18 * (days-1)

    elif 10 <= days <= 15:
        price = 18 * (days-1)

    elif days > 15:
        price = 18 * (days-1)
    

    if grade == "positive":
        price += 0.25 * price
    
    elif grade == 'negative':
        price -= 0.1 * price

elif type_of_room == 'apartment':
    if days < 10:
        price = 25 * (days-1)
        discount = 0.3 * price
        price -= discount

    elif 10 <= days <= 15:
        price = 25 * (days-1)
        discount = 0.35 * price
        price -= discount

    elif days > 15:
        price = 25 * (days-1)
        discount = 0.5 * price
        price -= discount
    

    if grade == "positive":
        price += 0.25 * price
    
    elif grade == 'negative':
        price -= 0.1 * price

elif type_of_room == 'president apartment':
    if days < 10:
        price = 35 * (days-1)
        discount = 0.1 * price
        price -= discount

    elif 10 <= days <= 15:
        price = 35 * (days-1)
        discount = 0.15 * price
        price -= discount

    elif days > 15:
        price = 35 * (days-1)
        discount = 0.2 * price
        price -= discount
    

    if grade == "positive":
        price += 0.25 * price
    
    elif grade == 'negative':
        price -= 0.1 * price
    
print(f"{price:.2f}")