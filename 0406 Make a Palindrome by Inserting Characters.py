class Solution:
    def solve(self, s):
        if not s: return 1
        ans = dict()

        def helper(l,r):
            if (l,r) in ans: return ans[(l,r)]
            if l >= r:
                ans[(l,r)] = 0
                return 0
            a = (min(helper(l,r-1), helper(l+1,r)) + 1) if s[l] != s[r] else helper(l+1,r-1)
            ans[(l,r)] = a
            return a

        return helper(0,len(s)-1)
