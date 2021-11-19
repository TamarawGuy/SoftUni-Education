n = int(input())
counter = 1

while counter <= n:
    print("*" * counter)
    counter += 1

counter -= 1
while counter > 1:
    print("*" * (counter-1))
    counter -= 1