class Solution:
    def solve(self, s):
        c = 0
        ans = 0

        for char in s:
          if char == "(":
            c += 1
          else: 
            c -= 1
            if c == -1:
              ans += 1
              c = 0

        return ans + c
