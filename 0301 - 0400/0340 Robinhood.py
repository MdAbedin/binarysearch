class Solution:
    def solve(self, n, e, o, t):
        year = 0
        
        while n < t:
            n += (e if year%2 == 0 else o)/100*n
            year += 1

        return year
