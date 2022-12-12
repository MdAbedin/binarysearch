class Solution:
    def solve(self, s):
        ans = []
        depth = -1

        for c in s:
          if c == "(":
            depth += 1
            if depth >= len(ans): ans.append(0)
          elif c == ")":
            depth -= 1
          else:
            ans[depth] += 1

        return ans
