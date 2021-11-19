######################
##### First way #####
######################

from functools import reduce


def multiply1(*args):
    return reduce(lambda x, y: x*y, args)

######################
##### Second way #####
######################


'''
def multiply(*args):
    num = 1
    for n in args:
        num *= n
    
    return num
'''

print(multiply1(1, 4, 5))
print(multiply1(4, 5, 6, 1, 3))