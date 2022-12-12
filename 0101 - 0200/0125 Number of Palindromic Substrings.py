class Solution:
    def solve(self, s):
        ans = 0

        for i in range(len(s)):
            j = 0
            while i-j >= 0 and i+j < len(s):
                if s[i-j] == s[i+j]: ans += 1
                else: break
                j += 1

            j = 0
            while i-j >= 0 and i+j+1 < len(s):
                if s[i-j] == s[i+j+1]: ans += 1
                else: break
                j += 1

        return ans
