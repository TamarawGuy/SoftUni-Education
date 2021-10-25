size = int(input())
days = int(input())
coins = 0
for i in range(1,days+1):
    if i % 10 == 0:
        size -= 2
    if i % 15 == 0:
        size += 5
    if i % 1 == 0:
        coins += 50
        coins -= 2 * size
    if i % 3 == 0:
        coins -= 3 * size
    if i % 5 == 0:
        coins += 20 * size
    if i % 3 == 0 and i % 5 == 0:
        coins -= 2 * size
    

print(f"{size} companions received {coins//size} coins each.")