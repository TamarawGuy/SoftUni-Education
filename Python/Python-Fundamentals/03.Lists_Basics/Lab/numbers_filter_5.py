n = int(input())
l = []
another_l = []
for i in range(n):
    number = int(input())
    l.append(number)

word = input()
if word == 'even':
    another_l = [x for x in l if x % 2 == 0]
    print(another_l)
elif word == 'odd':
    another_l = [x for x in l if x % 2 != 0]
    print(another_l)
elif word == 'negative':
    another_l = [x for x in l if x < 0]
    print(another_l)
elif word == 'positive':
    another_l = [x for x in l if x >= 0]
    print(another_l)