number = float(input())
from_what = input()
to_what = input()

if from_what == 'mm':
    if to_what == 'cm':
        result = number / 10
    
    elif to_what == 'm':
        result = number / 1000

elif from_what == 'cm':
    if to_what == 'mm':
        result = number * 10
    
    elif to_what == 'm':
        result = number / 100
    
elif from_what == 'm':
    if to_what == 'mm':
        result = number * 1000
    
    elif to_what == 'cm':
        result = number * 100
    
print(f"{result:.3f}")