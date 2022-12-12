class Solution:
    def solve(self, matrix):
        dp = [0]*len(matrix[0])

        for i in range(len(matrix)):
            dp = [min(dp[j], dp[j-1] if j-1 >= 0 else inf, dp[j+1] if j+1 < len(matrix[0]) else inf) + matrix[i][j] for j in range(len(matrix[0]))]

        return min(dp)
