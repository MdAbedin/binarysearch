class Solution:
    def solve(self, weights, values, capacity):
        dp = [0]*(capacity+1)

        for w,v in zip(weights,values):
            dp2 = dp[:]
            bests = [-v]*w

            for i in range(len(dp)):
                bests[i%w] = max(bests[i%w]+v, dp[i-w]+v if i-w >= 0 else 0)
                dp2[i] = max(dp2[i], bests[i%w])

            dp = dp2

        return max(dp)
