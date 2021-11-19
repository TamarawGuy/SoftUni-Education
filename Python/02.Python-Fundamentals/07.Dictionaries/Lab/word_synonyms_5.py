n = int(input())

d = {}

for i in range(n):
    word = input()
    synonym = input()

    if word not in d:
        d[word] = []
    d[word].append(synonym)
    
for word in d:
    print(f"{word} - {', '.join(d[word])}")