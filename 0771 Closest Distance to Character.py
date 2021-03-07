class Solution:
    def solve(self, s, c):
        last = int(-1e9)
        ans = []

        for i in range(len(s)):
            if s[i] == c: last = i
            ans.append(i-last)

        last = int(1e9)
        
        for i in range(len(s)-1,-1,-1):
            if s[i] == c: last = i
            ans[i] = min(ans[i], (last-i))

        return ans
