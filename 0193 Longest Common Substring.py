class Solution:
    def solve(self, s0, s1):
        dp = [0]*len(s0)
        ans = 0
        
        for i in range(len(s1)):
            dp2 = dp[:]

            for j in range(len(dp)):
                if s0[j] == s1[i]:
                    dp2[j] = 1 + (dp[j-1] if j-1 >= 0 else 0)
                    ans = max(ans, dp2[j])
                else:
                    dp2[j] = 0

            dp = dp2

        return ans
