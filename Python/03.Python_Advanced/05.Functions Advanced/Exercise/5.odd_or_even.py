def odd_or_even(c, nums):
    if c == 'Odd':
        return sum([x for x in nums if x % 2 == 1]) * len(nums)
    elif c == 'Even':
        return sum([x for x in nums if x % 2 == 0]) * len(nums)


command = input()
nums = [int(x) for x in input().split()]
print(odd_or_even(command, nums))