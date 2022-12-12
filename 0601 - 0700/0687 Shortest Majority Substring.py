class Solution:
    def solve(self, s):
        for i in range(1,len(s)):
            if s[i] == s[i-1]: return 2

        for i in range(2,len(s)):
            if s[i] == s[i-2]: return 3

        return -1
