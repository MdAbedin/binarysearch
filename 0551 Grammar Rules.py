class Solution:
    def solve(self, n):
        dp = [1,1,1,1,1]
        MOD = 10**9+7

        for i in range(n-1):
            new = [0,0,0,0,0]

            new[1] += dp[0]
            
            new[0] += dp[1]
            new[2] += dp[1]

            for j in range(5):
                if j != 2:
                    new[j] += dp[2]

            new[2] += dp[3]
            new[4] += dp[3]

            new[0] += dp[4]

            dp = new
            map(lambda x: x%MOD, dp)

        return sum(dp)%MOD
