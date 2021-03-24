my_str = input()
my_sum = 0

my_dict = {
    "a": 1,
    "e": 2,
    "i": 3,
    "o": 4,
    "u": 5,
}

for char in my_str:
    if char in my_dict:
        my_sum += my_dict[char]

print(my_sum)