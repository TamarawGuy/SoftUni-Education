vowels = 'aouei'
line = list(input())
print(''.join([x for x in line if x not in vowels]))