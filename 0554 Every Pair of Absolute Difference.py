class Solution:
    def solve(self, nums):
        if not nums: return 0

        MOD = 10**9+7
        rsum = sum(nums[i]-nums[0] for i in range(1,len(nums)))
        lsum = 0
        ans = lsum + rsum

        for i in range(1,len(nums)):
            diff = nums[i]-nums[i-1]
            lsum += i * diff
            rsum -= (len(nums)-i) * diff

            ans += lsum + rsum
            ans %= MOD

        return ans
