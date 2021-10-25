n = int(input())
def solve(num):
    if num < 100:
        number = 10 - (num//10)
        first_part = str(num) + "% "
        second_part = "[" + num//10 * "%"
        third_part = number * "." + "]"
        res = first_part + second_part + third_part
        return res, "Still loading..."

    elif num == 100:
        res = "100% Complete!"
        return res, "[%%%%%%%%%%]"
result = solve(n)
for item in result:
    print(item)