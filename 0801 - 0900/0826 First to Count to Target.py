class Solution:
    def solve(self, k, target):
        @lru_cache
        def helper(pts):
            if pts >= target-k: return True
            return any(not helper(pts + x) for x in range(1,k+1))

        return helper(0)
