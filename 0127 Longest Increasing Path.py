class Solution:
    def solve(self, matrix):
        dp = [[0]*len(matrix[0]) for i in range(len(matrix))]
        order = sorted([[y,x] for y in range(len(matrix)) for x in range(len(matrix[0]))], key=lambda coords: matrix[coords[0]][coords[1]])
        ans = 0

        for y,x in order:
          for ny,nx in [[y+1,x], [y-1,x], [y,x+1], [y,x-1]]:
            if 0<=ny<len(matrix) and 0<=nx<len(matrix[0]) and matrix[ny][nx] < matrix[y][x]:
              dp[y][x] = max(dp[y][x], dp[ny][nx])

          dp[y][x] += 1
          ans = max(ans, dp[y][x])

        return ans
