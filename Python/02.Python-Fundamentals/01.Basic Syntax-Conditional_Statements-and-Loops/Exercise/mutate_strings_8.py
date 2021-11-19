first = [x for x in input()]
second = [y for y in input()]

l = []

for i in range(len(first)):
    first[i] = second[i]
    whole_word = "".join(first)
    if whole_word not in l:
        l.append(whole_word)
    
for word in l:
    print(word)