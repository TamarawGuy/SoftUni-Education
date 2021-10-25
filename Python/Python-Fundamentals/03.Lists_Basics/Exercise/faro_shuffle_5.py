cards = input().split()
shuffles_count = int(input())
middle_length = len(cards) // 2
res = []

for i in range(shuffles_count):
    res = []
    for index in range(middle_length):
        first_card = cards[index]
        second_card = cards[index+middle_length]
        res.append(first_card)
        res.append(second_card)
    
    cards = res

print(res)