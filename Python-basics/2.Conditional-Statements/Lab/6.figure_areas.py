from math import pi

figure = input()

if figure == 'square':
    side = float(input())
    area = side * side
    print(f"{area:.3f}")

elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")

elif figure == 'circle':
    radius = float(input())
    area = pi * radius ** 2
    print(f"{area:.3f}")

elif figure == 'triangle':
    a = float(input())
    b = float(input())
    area = a * b / 2
    print(f"{area:.3f}")