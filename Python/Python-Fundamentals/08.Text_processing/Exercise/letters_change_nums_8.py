def check_letter(letter):
    if letter.isupper():
        return ord(letter) - 64
    else:
        return ord(letter) - 96
    
line = input().split()

results = []

for item in line:
    first_letter = item[0] # Upper - divide, lower - multiply
    second_letter = item[-1] # Upper - subtract, lower - add

    index_of_first_letter = check_letter(first_letter)
    index_of_second_letter = check_letter(second_letter)
    
    number = int(item[1:-1])
    
    if first_letter.isupper():
        res1 = float(number / index_of_first_letter)
    else:
        res1 = float(number * index_of_first_letter)
    
    if second_letter.isupper():
        final = res1 - index_of_second_letter
        results.append(final)
    else:
        final = res1 + index_of_second_letter
        results.append(final)
    
my_sum = sum(results)
print(f"{my_sum:.2f}")