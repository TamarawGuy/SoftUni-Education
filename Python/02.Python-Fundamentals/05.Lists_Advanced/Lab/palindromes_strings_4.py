line = input().split(" ")
word = input()
palindromes = []
for item in line:
    list_item = list(item)
    reversed_list_item = list(reversed(list_item))
    
    if list_item == reversed_list_item:
        palindromes.append(item)
    
print(palindromes)
occurences = palindromes.count(word)
print(f"Found palindrome {occurences} times")
