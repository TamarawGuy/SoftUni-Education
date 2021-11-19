def solve(ch1, ch2):
    num1 = ord(ch1)
    num2 = ord(ch2)
    
    for i in range(num1+1, num2+1):
        print(chr(i))

char1 = input()
char2 = input()

solve(char1, char2)