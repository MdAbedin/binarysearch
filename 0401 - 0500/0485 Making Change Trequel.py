class Solution:
    def solve(self, denominations, amount):
        MOD = 10**9+7
        ways = [1] + [0]*amount
        
        for coin in denominations:
            for amount in range(coin, len(ways)):
                ways[amount] += ways[amount-coin]
                ways[amount] %= MOD

        return ways[-1]
