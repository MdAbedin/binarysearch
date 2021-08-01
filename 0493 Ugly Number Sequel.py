class Solution:
    def solve(self, n):
        pq = [1]
        added = {1}

        for i in range(n):
            x = heappop(pq)
            for y in [2,3,5]:
                if x*y not in added:
                    added.add(x*y)
                    heappush(pq,x*y)

        return heappop(pq)
