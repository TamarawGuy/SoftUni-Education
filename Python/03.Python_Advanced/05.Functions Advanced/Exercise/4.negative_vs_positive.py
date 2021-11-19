def get_positive_sum(nums):
    positive_nums = [x for x in nums if x >= 0]
    return sum(positive_nums)


def get_negative_sum(nums):
    negative_sum = [x for x in nums if x < 0]
    return sum(negative_sum)


def compare_result(pos_sum, neg_sum):
    if pos_sum > abs(neg_sum):

        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"
    

nums = [int(x) for x in input().split()]
p_sum = get_positive_sum(nums)
n_sum = get_negative_sum(nums)
print(get_negative_sum(nums))
print(get_positive_sum(nums))
print(compare_result(p_sum, n_sum))