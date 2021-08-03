class Solution:
    def solve(self, prices):
        if not prices: return 0

        ans = [0,0,0,0]
        ans[3] -= prices[0]

        for i in range(1,len(prices)):
            ans2 = [0,0,0,0]
            ans2[0] = max(ans[0], ans[2])
            ans2[1] = ans[3] + prices[i]
            ans2[2] = ans[1]
            ans2[3] = max(ans[3], max(ans[0], ans[2]) - prices[i])
            ans = ans2
            # print(ans)

        return max(ans)
