class RangeSum:
    def __init__(self, nums):
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        self.prefix_sums = nums
        
    def total(self, i, j):
        if j == 0: return 0
        if i == 0: return self.prefix_sums[j-1]
        return self.prefix_sums[j-1]-self.prefix_sums[i-1]
