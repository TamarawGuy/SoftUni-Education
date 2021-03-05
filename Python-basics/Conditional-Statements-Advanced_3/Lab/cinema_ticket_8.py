day = input()

if day == "Wednesday" or day == "Thursday":
    ticket_price = 12

elif day == "Saturday" or day == "Sunday":
    ticket_price = 16

else:
    ticket_price = 12

print(ticket_price)