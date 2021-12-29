class Solution:
    def solve(self, n, k):
        dp = [[1] + [0]*k]

        for stair in range(1,n+1):
            next_ans = [0]*(k+1)

            for step in [1,2]:
                if stair - step >= 0:
                    for count in range(k+1):
                        next_ans[count] += dp[stair - step][count]

            if stair - 3 >= 0:
                for count in range(1,k+1):
                    next_ans[count] += dp[stair - 3][count-1]

            dp.append(next_ans)

        return sum(dp[-1])
