class Solution:
    def solve(self, nums):
        MOD = int(1e9+7)
        sublists = len(nums)
        ans = 0

        for i in range(len(nums)):
            ans += sublists*nums[i]
            ans %= MOD
            sublists += len(nums)-i-1 - (i+1)

        return ans
