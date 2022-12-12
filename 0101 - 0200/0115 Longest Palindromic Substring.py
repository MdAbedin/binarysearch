class Solution:
    def solve(self, s):
        return max((max((next(j for j in range(len(s)+1) if i+j == len(s) or i-j == -1 or s[i+j] != s[i-j])-1)*2+1,next(j for j in range(len(s)+1) if i+j+1 == len(s) or i-j == -1 or s[i+j+1] != s[i-j])*2) for i in range(len(s))), default=0)
