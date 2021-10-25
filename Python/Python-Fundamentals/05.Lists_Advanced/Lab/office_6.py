nums = [int(x) for x in input().split(" ")]
n = int(input())

multiplied_list = [x * 3 for x in nums]
avg_of_multiplied_list = sum(multiplied_list) / len(multiplied_list)
after_filtration_list = []
for num in multiplied_list:
    if num >= avg_of_multiplied_list:
        after_filtration_list.append(num)
    
if len(after_filtration_list) >= len(multiplied_list)/2:
    print(f"Score: {len(after_filtration_list)}/{len(nums)}. Employees are happy!")
else:
    print(f"Score: {len(after_filtration_list)}/{len(nums)}. Employees are not happy!")