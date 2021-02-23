def split_and_join(line):
    # write your code here
    arr = line.split()
    return '-'.join(arr)

print(split_and_join('this is a string'))