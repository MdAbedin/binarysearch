class RangeSum:
    def __init__(self, nums):
        self.nums = [0] + nums
        for i in range(1,len(self.nums)):
            self.nums[i] += self.nums[i-1]

    def total(self, i, j):
        return self.nums[j]-self.nums[i]
