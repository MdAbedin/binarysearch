class Solution:
    def solve(self, a, b):
        if not a or not b: return len(a)+len(b)
        
        dp = [0]*len(a)

        for i in range(len(b)):
            dp2 = dp[:]

            for j in range(len(dp)):
                if b[i]==a[j]:
                    dp2[j] = max(dp[j],dp2[j-1] if j-1>=0 else 0,1+(dp[j-1] if j-1>=0 else 0))
                else:
                    dp2[j] = max(dp[j],dp2[j-1] if j-1>=0 else 0)

            dp = dp2

        return len(a)+len(b)-2*dp[-1]
