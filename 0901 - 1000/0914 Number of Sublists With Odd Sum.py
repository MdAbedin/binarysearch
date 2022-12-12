class Solution:
    def solve(self, nums):
        counts = [1,0]
        psum = 0
        ans = 0
        MOD = 10**9+7

        for num in nums:
            psum += num
            ans += counts[1-(psum%2)]
            ans %= MOD
            counts[psum%2] += 1

        return ans
