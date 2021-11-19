#####################
##### First way #####
#####################

def convert_to_list_of_abs_values(l1):
    return [abs(num1) for num1 in l1]


nums1 = [float(x) for x in input().split()]
print(convert_to_list_of_abs_values(nums1))


#####################
##### Second way #####
#####################

def convert_to_list_of_abs_values(l2):
    return list(map(lambda x: abs(x), l2))


nums2 = map(lambda el: float(el), input().split())
print(convert_to_list_of_abs_values(nums2))