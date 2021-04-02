def runningSum(nums):
    s = 0
    lst = []
    for i in nums:
        s += i
        lst.append(s)
    return(lst)
    
print(runningSum([1,2,3,4,5]))