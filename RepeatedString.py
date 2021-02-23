def repeatedString(s, n):
    if s == 'a':
        return n
    else:
        while len(s) <= n:
            for letter in s:
                s += letter
    
    s = s[:n]
    # print(s)
    num_a = s.count('a')
    return(num_a)

print(repeatedString('aba', 10))
print(repeatedString('aba', 12))
print(repeatedString('a', 10))
print(repeatedString('aa', 10))