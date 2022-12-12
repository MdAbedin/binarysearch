class Solution:
    def solve(self, s):
        if s in ["1","0"]: return 0
        x = s.rfind("1")
        
        if x == 0:
            return len(s)-1
        else:
            return len(s) + s[:x].count("0") + 1
