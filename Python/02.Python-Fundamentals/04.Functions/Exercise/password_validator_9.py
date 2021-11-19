def check_password(password):
    valid_len = False
    valid_letters_digits = False
    valid_2_digits = False
    l = []
    my_str = ''

    if len(password) >= 6 and len(password) <= 10:
        valid_len = True

    for letter in password:
        num = ord(letter)
        if 48 <= num <= 57:
            valid_letters_digits = True
        elif 65 <= num <= 90:
            valid_letters_digits = True
        elif 97 <= num <= 122:
            valid_letters_digits = True
        else:
            valid_letters_digits = False
            break

    for let in password:
        num = ord(let)
        if 48 <= num <= 57:
            l.append(num)
            if len(l) >= 2:
                valid_2_digits = True
        
    if valid_len == valid_letters_digits == valid_2_digits:
        my_str = "Password is valid"
    else:
        if valid_len == False:
            my_str += "Password must be between 6 and 10 characters\n"
        if valid_letters_digits == False:
            my_str += "Password must consist only of letters and digits\n"
        if valid_2_digits == False:
            my_str += 'Password must have at least 2 digits'
        
    return my_str

p = input()
print(check_password(p))