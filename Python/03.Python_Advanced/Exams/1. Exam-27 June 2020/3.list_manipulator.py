def list_manipulator(nums, *args):
    if len(args) == 2:
        where = args[1]

        if where == "beginning":
            del nums[0]
            return nums
        elif where == 'end':
            del nums[-1]
            return nums
        
    else:
        command = args[0]
        if command == 'add':
            where = args[1]
            additional_nums = list(args[2:])
            if where == "beginning":
                additional_nums += nums
                return additional_nums

            elif where == 'end':
                nums += additional_nums
                return nums

        elif command == "remove":
            where = args[1]
            num = args[2]

            if where == "beginning":
                return nums[num:]

            elif where == "end":
                return nums[:-num]




print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
