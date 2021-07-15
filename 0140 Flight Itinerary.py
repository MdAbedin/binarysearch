class Solution:
    def solve(self, flights):
        if not flights: return []
        start = set(flight[0] for flight in flights) - set(flight[1] for flight in flights)
        g = {a:b for a,b in flights}
        cur = next(iter(start))
        ans = [cur]
        while cur in g:
            cur = g[cur]
            ans.append(cur)
        return ans
