class Solution:
    def solve(self, nums, k):
        MOD = 10**9 + 7
        pair_sums = [nums[i]+nums[i+1] for i in range(len(nums)-1)]
        ans = 0

        for i in range(len(pair_sums)-1):
            decrements = min(nums[i+1], max(0, pair_sums[i] - k))
            pair_sums[i] -= decrements
            pair_sums[i+1] -= decrements
            ans += decrements
            ans %= MOD

        decrements = min(nums[0], max(0, pair_sums[0] - k))
        pair_sums[0] -= decrements
        ans += decrements
        ans %= MOD

        if len(nums)-1 != 0:
            decrements = min(nums[-1], max(0, pair_sums[-1] - k))
            pair_sums[-1] -= decrements
            ans += decrements
            ans %= MOD
        
        return ans
