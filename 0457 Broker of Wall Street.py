class Solution:
    def solve(self, prices, fee):
        if not prices: return 0

        max_holding = -inf
        max_not_holding = 0

        for price in prices:
            max_holding, max_not_holding = max(max_holding, max_not_holding - price), max(max_not_holding, max_holding + price - fee)

        return max_not_holding
