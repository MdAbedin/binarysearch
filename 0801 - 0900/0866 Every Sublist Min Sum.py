class Solution:
    def solve(self, nums):
        if not nums: return 0

        MOD = 10**9+7
        stack = []
        first_smaller_right = [-1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack: first_smaller_right[i] = stack[-1]
            stack.append(i)

        dp = [None] * len(nums)
        ans = 0
        
        for i in range(len(nums)-1,-1,-1):
            if first_smaller_right[i] == -1:
                dp[i] = nums[i]*(len(nums)-i)
            else:
                dp[i] = dp[first_smaller_right[i]] + nums[i] * (first_smaller_right[i] - i)

            dp[i] %= MOD
            ans += dp[i]
            ans %= MOD

        return ans
