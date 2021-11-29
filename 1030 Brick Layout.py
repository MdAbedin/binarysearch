class Solution:
    def solve(self, bricks, width, height):
        dp = [0]*(width+1)
        dp[0] = 1

        for i in range(len(dp)):
            for brick in bricks:
                dp[i] += dp[i-brick] if i-brick >= 0 else 0

        return dp[-1]**height
