def repeatedString(s, n):
    return (n // len(s)) * s.count('a') + s[:(n % len(s))].count('a')
    
print(repeatedString('aba', 10))
print(repeatedString('a', 10))
print(repeatedString('aa', 10))