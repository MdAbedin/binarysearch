class Solution:
    def solve(self, s):
        ans = 0

        for c in s:
          ans *= 26
          ans += ord(c)-ord('A')+1

        return ans
