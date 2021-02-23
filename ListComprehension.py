x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])


# Sample Input 

# 1
# 1
# 1
# 2

# Sample Output

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]