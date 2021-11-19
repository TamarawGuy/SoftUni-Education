s = list(input())
d = ''
l = ''
o = ''

for ch in s:
    if ch.isdigit():
        d += ch
    elif ch.isalpha():
        l += ch
    else:
        o += ch
    
print(d)
print(l)
print(o)