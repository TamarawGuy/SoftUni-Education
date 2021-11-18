line = input().split(" ")
search = input().split(" ")

d = dict()

for i in range(0, len(line), 2):
    d[line[i]] = int(line[i+1])

for item in search:
    if item in d:
        print(f"We have {d[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")