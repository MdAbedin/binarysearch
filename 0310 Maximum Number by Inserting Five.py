class Solution:
    def solve(self, n):
        n = str(n)

        for i in range(0 if n[0]!="-" else 1,len(n)):
          if (int(n[i]) < 5 if n[0]!="-" else int(n[i]) > 5): return int(n[:i] + "5" + n[i:])

        return int(n + "5")
