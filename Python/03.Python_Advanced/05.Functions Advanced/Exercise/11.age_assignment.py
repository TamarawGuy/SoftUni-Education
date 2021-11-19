def age_assignment(*args, **kwargs):
    d = {}
    for name in args:
        for char, age in kwargs.items():
            if name.startswith(char):
                d[name] = age
    
    return d

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
