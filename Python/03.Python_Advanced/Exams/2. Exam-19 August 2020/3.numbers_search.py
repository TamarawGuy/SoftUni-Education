def numbers_searching(*args):
    min_num = min(args)
    max_num = max(args)
    l_of_duplicates = []

    for i in range(min_num, max_num):
        if i not in args:
            missing_number = i
            break
    
    for item in args:
        if args.count(item) >= 2 and item not in l_of_duplicates:
            l_of_duplicates.append(item)
        
    
    return [missing_number, sorted(l_of_duplicates)]




print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
