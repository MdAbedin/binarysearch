class Solution:
    def solve(self, nums):
        nums_set = set(nums)
        return [x for x in range(1,len(nums)+1) if x not in nums_set]
