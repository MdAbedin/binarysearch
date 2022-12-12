class Solution:
    def solve(self, nums):
        if len(nums) <= 3: return min(nums, default = 0)

        dp = [0,0,0]

        for num in nums: dp.append(min(dp[-3:]) + num)

        return min(dp[-3:])
