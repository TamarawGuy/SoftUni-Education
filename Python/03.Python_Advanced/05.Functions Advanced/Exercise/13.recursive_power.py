#####################
##### FIRST WAY #####
#####################


def recursive_power(number, power):
    
    if power == 0:
        return 1
    if power >= 0:
        return number * recursive_power(number, power-1)

print(recursive_power(2, 10))
print(recursive_power(10, 100))


######################
##### SECOND WAY #####
######################


def recursive_power2(number2, power2):
    if power2 == 0:
        return 1
    return number2 * recursive_power2(number2, power2-1)


print(recursive_power2(2, 10))
print(recursive_power2(10, 100))