class Solution:
    def solve(self, coins, quantities):
        ans = {0}

        for coin, count in zip(coins, quantities):
            for _ in range(count):
                new_ans = set(ans)
                for amount in ans:
                    new_ans.add(amount + coin)
                ans = new_ans

        return len(ans)-1
