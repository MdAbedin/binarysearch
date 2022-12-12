class Solution:
    def solve(self, n):
        return any((n-i*3)%7 == 0 for i in range(n//3+1))
