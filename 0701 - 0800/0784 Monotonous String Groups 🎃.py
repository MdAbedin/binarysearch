class Solution:
    def solve(self, s):
        ans = 0
        i = 0

        while i < len(s):
          ans += 1
          first = s[i]
          
          while i < len(s) and s[i] == first: i += 1
          if i >= len(s): break
          
          d = 1 if s[i] > s[i-1] else -1
          while i < len(s) and (s[i] >= s[i-1] if d == 1 else s[i] <= s[i-1]): i += 1

        return ans
