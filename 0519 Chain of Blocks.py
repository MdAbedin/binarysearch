class Solution:
    def solve(self, blocks):
        dp = defaultdict(int)

        for a,b in blocks:
            dp[b] = max(dp[b], dp[a]+1)

        return max(dp.values(),default=0)
