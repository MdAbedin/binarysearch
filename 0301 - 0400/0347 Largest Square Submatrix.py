class Solution:
    def solve(self, matrix):
        dp = [[[0,0,0] for x in range(len(matrix[0])+1)] for y in range(len(matrix)+1)]
        ans = 0

        for y in range(len(matrix)):
          for x in range(len(matrix[0])):
            if matrix[y][x] == 1:
              dp[y][x] = [min(dp[y-1][x-1][0], dp[y-1][x][1], dp[y][x-1][2]) + 1, dp[y-1][x][1]+1, dp[y][x-1][2]+1]
              ans = max(ans, dp[y][x][0])

        return ans**2
