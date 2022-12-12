class Solution:
    def solve(self, s):
        if len(s) < 3: return 0

        vals = [-1,-1,-1,-1]
        if s[1] == "0":
            if s[0] == "0":
                vals = [1,0,1,2]
            else:
                vals = [0,1,2,1]
        else:
            if s[0] == "0":
                vals = [2,1,0,1]
            else:
                vals = [1,2,1,0]
        
        for i in range(2,len(s)):
            if s[i] == "0":
                vals = [min(vals[2],vals[3]),vals[0],1+min(vals[0],vals[1]),1+vals[2]]
            else:
                vals = [1+min(vals[2],vals[3]),1+vals[0],min(vals[0],vals[1]),vals[2]]

        return min(vals)
