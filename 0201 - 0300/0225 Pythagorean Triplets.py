class Solution:
    def solve(self, nums):
        nums_set = set(nums)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if sqrt(nums[i]**2+nums[j]**2) in nums_set: return True

        return False
