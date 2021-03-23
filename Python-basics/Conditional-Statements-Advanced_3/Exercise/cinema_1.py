type_projection = input()
rows = int(input())
cols = int(input())

if type_projection == "Premiere":
    result = rows * cols * 12
elif type_projection == "Normal":
    result = rows * cols * 7.50
elif type_projection == "Discount":
    result = rows * cols * 5

print(f"{result:.2f} leva")