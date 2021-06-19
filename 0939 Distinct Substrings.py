class Solution:
    def solve(self, s):
        return len({s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)})
