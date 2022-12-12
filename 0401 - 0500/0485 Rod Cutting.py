class Solution:
    def solve(self, prices, n):
        prices = [0]+prices

        for i in range(2,n+1):
          for j in range(1,i):
            prices[i] = max(prices[i], prices[j]+prices[i-j])

        return prices[-1]
