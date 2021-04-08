class Solution:
    def solve(self, nums):
        dp = [0,0]

        for i in range(len(nums)):
            dp.append(max(0,nums[i]+dp[-2],dp[-1]))

        return max(dp)
