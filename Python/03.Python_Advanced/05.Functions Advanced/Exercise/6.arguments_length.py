def args_length(*number_of_args):
    return len(number_of_args)


print(args_length(1, 32, 5))
print(args_length("john", "peter"))
print(args_length([1, 2, 3]))
