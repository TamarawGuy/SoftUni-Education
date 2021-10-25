l_even = []
l_odd = []
def solve(num):
    for n in num:
        int_n = int(n)
        if int_n % 2 == 0:
            l_even.append(int_n)
        else:
            l_odd.append(int_n)
    return f"Odd sum = {sum(l_odd)}, Even sum = {sum(l_even)}"

number = input()
print(solve(number))