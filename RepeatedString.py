def repeatedString(s, n):
    if s == 'a':
        return n
    else:
        while len(s) <= n:
            for letter in s:
                s += letter
    
    s = s[:n+1]
    num_a = s.count('a')
    return(num_a)

print(repeatedString('aba', 10))
print(repeatedString('a', 1000))
print(repeatedString('aa', 1000))