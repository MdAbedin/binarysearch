class Solution:
    def solve(self, nums, target):
        nums = [0]+nums
        dp = [0]
        lasts = {0:0}
        psum = 0

        for i in range(1,len(nums)):
            ans = dp[-1]
            psum += nums[i]

            if psum-target in lasts: ans = max(ans, dp[lasts[psum-target]] + 1)

            lasts[psum] = i
            dp.append(ans)

        return dp[-1]
