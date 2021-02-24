def rotLeft(a, d):
    k = len(a) - d%len(a)
    C=[*range(len(a))]
    print('Ilk hali', C)
    for i,j in enumerate(a):
        m=i+k
        print('m', m)
        if len(C)<=m: C[m%len(C)]=j
        else: C[m]=j
        print('C', C)
    return C

print(rotLeft([2,3,4,5], 1))