class Solution:
    @lru_cache
    def solve(self, n):
        return n if n <= 4 else max(self.solve(n-4)*4, self.solve(n-3)*3)
