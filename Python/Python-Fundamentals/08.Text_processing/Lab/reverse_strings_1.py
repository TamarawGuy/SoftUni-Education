l = []

while True:
    word = input()
    if word == 'end':
        break

    l_word = list(word)
    reversed_word = "".join(list(reversed(word)))
    print(f"{word} = {reversed_word}")