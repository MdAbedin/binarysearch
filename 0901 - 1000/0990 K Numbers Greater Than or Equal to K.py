class Solution:
    def solve(self, nums):
        nums.sort()

        if nums[-1] < 0: return 0

        for k in range(1,len(nums)+1):
            if k != len(nums) and nums[~k] >= k: continue
            if nums[~k+1] >= k: return k

        return -1
