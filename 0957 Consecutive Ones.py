class Solution:
    def solve(self, nums):
        if 1 not in nums: return True
        i = nums.index(1)+1

        while i < len(nums):
            if nums[i]==1 and nums[i-1] != 1: return False
            i += 1

        return True
