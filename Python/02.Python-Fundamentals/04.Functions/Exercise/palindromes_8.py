def solve(numbers):
    l = []
    for number in numbers:
        l_number = list(number)
        reversed_number = "".join(list(reversed(l_number)))
        if reversed_number == number:
            l.append(True)
        else:
            l.append(False)
    for item in l:
        print(item)

line = input().split(", ")

solve(line)