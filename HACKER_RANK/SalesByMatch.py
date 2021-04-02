n = 5
arr = [5, 5, 3, 4, 4, 4]

s = 0
for i in set(arr):
    num = arr.count(i)
    pair_num = num // 2
    if pair_num > 0:
        s += 1

print(s)