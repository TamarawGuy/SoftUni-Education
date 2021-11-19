def reverse_numbers(nums):
    stack = []
    reversed_list = []
    for item in nums:
        stack.append(item)
    while len(stack) > 0:
        num = stack.pop()
        reversed_list.append(num)
    
    return reversed_list


def print_result(result):
    print(*result)


numbers = [int(x) for x in input().split()]
reversed_numbers = reverse_numbers(numbers)
print_result(reversed_numbers)