class Solution:
    def solve(self, n):
        if n <= 4: return n
        return max(self.solve(n-4)*4, self.solve(n-3)*3)
