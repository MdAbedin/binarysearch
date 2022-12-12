class Solution:
    def solve(self, n):
        MOD = 10**9+7
        a,b = 0,1

        for i in range(n):
            a,b = b, (a+b)%MOD

        return b
