class Solution:
    def solve(self, nums):
        if nums[1]-nums[0] < 0: return False
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]: return False

        return True
