class Solution:
    def solve(self, weights, values, capacity):
        dp = [0]*(capacity+1)

        for v,w in zip(values,weights):
            dp2 = dp[:]

            for i in range(w,len(dp)):
                dp2[i] = max(dp[i],dp[i-w]+v)

            dp = dp2

        return max(dp)
