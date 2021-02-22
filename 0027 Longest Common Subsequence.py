class Solution:
    def solve(self, a, b):
        if not a or not b: return 0
        
        dp = [0]*len(a)

        for i in range(len(b)):
          dp2 = dp[:]

          for j in range(len(a)):
            dp2[j] = max(dp2[j], (dp[j-1] if j-1>=0 else 0) + (1 if b[i] == a[j] else 0), dp2[j-1] if j-1 >= 0 else 0)

          dp = dp2

        return dp[-1]
