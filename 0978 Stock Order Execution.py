class Solution:
    def solve(self, orders):
        buys,sells = [],[]
        ans = 0

        for p,a,t in orders:
            if t == 0:
                while a and sells and sells[0][0] <= p:
                    total = min(sells[0][1], a)
                    a -= total
                    ans += total
                    sells[0][1] -= total
                    if sells[0][1] == 0: heappop(sells)

                if a > 0:
                    heappush(buys,[-p,a])
            else:
                while a and buys and -buys[0][0] >= p:
                    total = min(buys[0][1], a)
                    a -= total
                    ans += total
                    buys[0][1] -= total
                    if buys[0][1] == 0: heappop(buys)

                if a > 0:
                    heappush(sells,[p,a])

        return ans
