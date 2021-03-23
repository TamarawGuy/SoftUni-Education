degrees = int(input())
when = input()

if 10 <= degrees <= 18:
    if when == "Morning":
        print(f"It's {degrees} degrees, get your Sweatshirt and Sneakers.")
    elif when == "Afternoon":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif when == "Evening":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")

elif 18 < degrees <= 24:
    if when == "Morning":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif when == "Afternoon":
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
    elif when == "Evening":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
        
elif degrees >= 25:
    if when == "Morning":
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
    elif when == "Afternoon":
        print(f"It's {degrees} degrees, get your Swim Outfit and Barefoot.")
    elif when == "Evening":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
        