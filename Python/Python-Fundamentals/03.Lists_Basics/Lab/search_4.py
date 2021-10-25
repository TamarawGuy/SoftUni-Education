n = int(input())
word = input()
l = []
l_word = []
for i in range(n):
    line = input()
    l.append(line) 
    if word in line:
        l_word.append(line)
    
print(l)
print(l_word)