#####################
##### First way #####
#####################

def round_values_in_list(l1):
    return [round(num1) for num1 in l1]


nums1 = [float(x) for x in input().split()]
print(round_values_in_list(nums1))


#####################
##### Second way #####
#####################

def round_values_in_list(l2):
    return list(map(lambda x: round(x), l2))


nums2 = map(lambda x: float(x), input().split())
print(round_values_in_list(nums2))