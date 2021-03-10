class Solution:
    def solve(self, s):
        if not s: return ""
        
        s = list(s)
        mins = []
        cur_min = len(s)-1
        
        for i in range(len(s)-2,-1,-1):
            mins.append(cur_min)
            if s[i] < s[cur_min]: cur_min = i

        mins.reverse()

        for i in range(len(s)-1):
            if s[mins[i]] < s[i]:
                s[i], s[mins[i]] = s[mins[i]], s[i]
                return "".join(s)

        return "".join(s)
