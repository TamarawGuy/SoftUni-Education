from collections import deque


def best_list_pureness(nums, k):
    nums = deque(nums)
    best_pureness = -1000000000000000000000
    best_index = -1

    for i in range(k):
        for item in nums:
            item_index = nums.index(item)
            pureness += item * item_index

        if pureness > best_pureness:
            best_pureness = pureness
            best_index = i
        
        nums.appendleft(nums.pop())

    return f"Best pureness {best_pureness} after {best_index} rotations"


test = ([4, 1, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
