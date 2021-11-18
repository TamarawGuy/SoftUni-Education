line = list(input())
emoticons = []

for i in range(len(line)):
    if line[i] == ':':
        symbol = line[i] + line[i+1]
        emoticons.append(symbol)

for em in emoticons:
    print(em)