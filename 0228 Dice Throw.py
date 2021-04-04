MOD = int(1e9+7)

class Solution:
    @cache
    def solve(self, n, faces, total):
        if n == 0: return 1 if total == 0 else 0
        return sum(self.solve(n-1,faces,total-face) for face in range(1,faces+1)) % MOD
