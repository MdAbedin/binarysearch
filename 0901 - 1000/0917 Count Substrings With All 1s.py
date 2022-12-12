class Solution:
    def solve(self, s):
        MOD = 10**9+7
        streak = 0
        ans = 0
        for c in s:
            if c == "1": streak += 1
            else: streak = 0
            ans += streak
            ans %= MOD
        return ans
