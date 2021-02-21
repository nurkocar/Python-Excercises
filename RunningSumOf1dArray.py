    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        lst = []
        for i in nums:
            s += i
            lst.append(s)
        return(lst)