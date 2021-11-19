def min_number_in_numbers(nums):
    return min(nums)


def max_number_in_numbers(nums):
    return max(nums)


def sum_number_in_numbers(nums):
    return sum(nums)


nums = [int(x) for x in input().split()]
print(f"The minimum number is {min_number_in_numbers(nums)}")
print(f"The maximum number is {max_number_in_numbers(nums)}")
print(f"The sum number is: {sum_number_in_numbers(nums)}")