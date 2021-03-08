class Solution:
    def solve(self, prices):
        if not prices: return 0

        mn = prices[0]
        ans = 0

        for price in prices:
            mn = min(mn, price)
            ans = max(ans, price-mn)

        return ans
