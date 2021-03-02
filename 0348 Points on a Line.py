class Solution:
    def solve(self, coordinates):
        if not coordinates: return 0
        coordinates.sort()
        dp = defaultdict(lambda: defaultdict(lambda: 1))
        ans = 1

        for i in range(len(coordinates)):
          x1,y1 = coordinates[i]

          for j in range(i):
            x2,y2 = coordinates[j]
            slope = "DNE" if x1==x2 else (y1-y2)/(x1-x2)
            dp[i][slope] = dp[j][slope] + 1
            ans = max(ans, dp[i][slope])

        return ans
