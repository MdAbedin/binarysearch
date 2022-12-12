class Solution:
    def solve(self, s):
        if not s: return 0
        
        x = 0
        xr = s.count("x")
        ans = inf
        
        for i in range(len(s)+1):
            ans = min(ans, abs(i-x) + xr)
            if i == len(s): break
            if s[i] == "x":
                x += 1
                xr -= 1

        return ans
