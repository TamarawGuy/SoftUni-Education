import math

def func1(number):
    my_list = []
    while True:
        number = math.ceil(number / 2)
        my_list.append(number)
        if number == 1:
            break
    reversed_list = list(reversed(my_list))
    return my_list


def check(number):
    my_list1 = func1(number)
    final_list = []
    is_valid = False
    for i in range(len(my_list1)):
        num = my_list1[i]
        if number % num == 0:
            is_valid = True
            final_list.append(my_list1[i])
        else:
            is_valid = False
            break
    reversed_list = list(reversed(final_list))
    return is_valid, reversed_list


number = int(input())
my_tuple = check(number)
if my_tuple[0] == True:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")