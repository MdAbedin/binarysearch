class Solution:
    def solve(self, prices):
        ans = [0]*len(prices)
        unmatched = []

        for i in range(len(prices)):
            while unmatched and unmatched[0][0] < prices[i]:
                j = heappop(unmatched)[1]
                ans[j] = i-j
            heappush(unmatched,[prices[i],i])

        return ans
