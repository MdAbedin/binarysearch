class Solution:
    def solve(self, s):
        leftmosts = dict()
        rightmosts = dict()
        ans = 0
        c = 0

        for i in range(len(s)):
          if s[i] == "(":
            if c not in leftmosts: leftmosts[c] = i
            rightmosts[c] = i
            c += 1
          else:
            c -= 1
            if c in leftmosts: ans = max(ans, i - leftmosts[c] + 1)
            rightmosts[c] = i
            leftmosts.pop(c+1, None)

        return ans
