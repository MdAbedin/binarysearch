class Solution:
    def solve(self, n, k):
        MOD = 10**9+7
        dp = [0]*(k+1)
        dp[0] = 1

        for i in range(n):
            dp2 = [0]*(k+1)
            dp2[0] = sum(dp)%MOD
            
            for i in range(1,k+1):
                dp2[i] = dp[i-1]

            dp = dp2

        return sum(dp)%MOD
