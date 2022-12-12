class Solution:
    def solve(self, nums, k, target):
        return ceil(abs((target-sum(nums))/k))
