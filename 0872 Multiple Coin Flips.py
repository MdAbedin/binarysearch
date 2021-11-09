class Solution:

    def solve(self, chances, target):

        dp = [0]*(target+1)

        dp[0] = 1

        for i in range(len(chances)):

            new_dp = [0]*len(dp)

            for j in range(len(new_dp)):

                if j-1 >= 0: new_dp[j] += dp[j-1]*chances[i]

                new_dp[j] += dp[j]*(1-chances[i])

            dp = new_dp

        return dp[-1]
