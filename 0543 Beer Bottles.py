class Solution:
    def solve(self, n):
        ans = 0
        f,e = n,0

        while f > 0:
            ans += f
            e += f
            f = e//3
            e = e%3

        return ans
