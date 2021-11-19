def solve(s, V):
    return "".join([ch for ch in s if ch not in V])


word = input()
VOWELS = 'aoueiAOUEI'
print(solve(word, VOWELS))