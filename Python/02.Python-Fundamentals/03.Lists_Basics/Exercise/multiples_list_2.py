factor = int(input())
start = factor
end = int(input())
l = []
counter = 0
while counter < end:
    l.append(start)
    start += factor
    counter += 1
print(l)