class Solution:
    def solve(self, s):
        cnt = 0

        for c in s:
          if c == "(":
            cnt += 1
          else:
            cnt -= 1
            if cnt < 0: return False

        return cnt == 0
