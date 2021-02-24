# n = int(input())
# arr = map(int, input().split())

# FIRST SOLUTION
# n = 4
# arr = [2, 5, 5, 6]
# arr = set(arr)
# runner_up = sorted(arr)[-2:-1]
# print(runner_up)
# print(runner_up[0])

# instead of number 7 8 and 9 lines number 12 can be used 
# print(sorted(arr)[-2:-1][0])

# Sample Input 

# 5
# 2 3 6 6 5

# Sample Output 

# 5

# SECOND SOLUTION

arr = [5, 2, 5, 6, 3]

# arr = set(arr)
# print(arr)
# arr = sorted(arr)
# print(arr)
# print(arr[-2])

print(sorted(set(arr))[-2])

