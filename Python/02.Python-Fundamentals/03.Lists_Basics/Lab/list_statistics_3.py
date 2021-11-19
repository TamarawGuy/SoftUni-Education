n = int(input())

l_p = []
l_n = []

for i in range(n):
    number = int(input())
    if number >= 0:
        l_p.append(number)
    else:
        l_n.append(number)
print(l_p)
print(l_n)
print(f"Count of positives: {len(l_p)}. Sum of negatives: {sum(l_n)}")