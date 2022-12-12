class Solution:
    def solve(self, nums):
        dp = [True]
        nums = [None] + nums

        for i in range(1,len(nums)):
            curr = False

            if i-2 >= 0 and nums[i] == nums[i-1] and dp[i-2]: curr = True
            if i-3 >= 0 and dp[i-3]:
                if nums[i] == nums[i-1] == nums[i-2]: curr = True
                if nums[i-2:i] == [nums[i]-2,nums[i]-1]: curr = True

            dp.append(curr)

        return dp[-1]
