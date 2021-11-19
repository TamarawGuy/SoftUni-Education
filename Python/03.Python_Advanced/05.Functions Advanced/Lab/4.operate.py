from functools import reduce

#################################
########### First way ###########
##### WITHOUT EVAL FUNCTION #####
#################################

def operate1(operator, *nums1):
    if operator == '+':
        return sum(nums)
    elif operator == '-':
        return reduce(lambda x, y: x - y, nums1)
    elif operator == '*':
        return reduce(lambda x, y: x * y, nums1)
    elif operator == '/':
        return reduce(lambda x, y: x / y, nums1)
    
print(operate1("+", 1, 2, 3))
print(operate1("*", 3, 4))
print(operate1("/", 3, 4))


##############################
######### Second way #########
##### WITH EVAL FUNCTION #####
##############################

def operate2(operator, *nums2):
    return reduce(lambda x, y: eval(f"{x} {operator} {y}"), nums2)


print(operate2("+", 1, 2, 3))
print(operate2("*", 3, 4))
print(operate2("/", 3, 4))



#################################
########### Third way ###########
##### WITHOUT IF STATEMENTS #####
#################################

mapper = {
    "+": lambda x, y: x + y,
    '-': lambda x, y: x - y,
}

def operate3(operator, *nums3):
    return reduce(mapper[operator], nums3)


print(operate3('+', 1, 2, 3))