class Solution:
    def helper(self, s, n):
        if len(s) == 0: return [[n > 1,-inf]]
        if s[0] == "0": return [[len(s)==1,0]]

        ans = []

        for i in range(len(s)):
            ans2 = self.helper(s[i+1:],n+1)
            
            for works,mx in ans2:
                if works and (mx == int(s[:i+1])-1 or mx == -inf): ans.append([True,int(s[:i+1])])

        if ans: return ans

        return [[False,-1]]


    def solve(self, s):
        return any(x[0] for x in self.helper(s,0))
