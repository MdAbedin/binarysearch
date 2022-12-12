class Solution:
    def solve(self, n):
        if n == 0:
            return 1

        MOD =10**9+7
        dp = [1]

        for i in range(1,n+1):
            ans = 0

            for j in range(i):
                ans += dp[j]*dp[i-j-1]
                ans %= MOD

            dp.append(ans)

        return dp[-1]
