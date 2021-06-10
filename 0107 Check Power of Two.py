class Solution:
    def solve(self, n):
        if n==0:return False
        return log(n,2)==int(log(n,2))
