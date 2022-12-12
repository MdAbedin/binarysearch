class Solution:
    def solve(self, matrix):
        dp = [[[None,0,0,0] for x in range(len(matrix[0])+1)] for y in range(len(matrix)+1)]
        ans = 0

        for y in range(len(matrix)):
          for x in range(len(matrix[0])):
            coeff0 = 1 if matrix[y][x] == dp[y-1][x][0] == dp[y][x-1][0] == dp[y-1][x-1][0] else 0
            coeff1 = 1 if matrix[y][x] == dp[y-1][x][0] else 0
            coeff2 = 1 if matrix[y][x] == dp[y][x-1][0] else 0
            
            dp[y][x] = [matrix[y][x], coeff0*min(dp[y-1][x-1][1], dp[y-1][x][2], dp[y][x-1][3]) + 1, coeff1*dp[y-1][x][2] + 1, coeff2*dp[y][x-1][3]+1]
            ans = max(ans, dp[y][x][1])

        return ans
