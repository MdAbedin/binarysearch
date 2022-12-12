class Solution:
    def solve(self, edges, success, start, end):
        if start == end: return 1

        g = defaultdict(list)

        for (a,b),chance in zip(edges,success):
            g[a].append([b,chance])
            g[b].append([a,chance])

        pq = [[-1,start]]
        bests = defaultdict(int)
        ans = 0

        while pq:
            chance,cur = heappop(pq)
            chance *= -1

            if chance < bests[cur]: continue

            for nei,nei_chance in g[cur]:
                if nei == end:
                    ans = max(ans, chance * nei_chance)
                elif chance * nei_chance > bests[nei]:
                    bests[nei] = chance * nei_chance
                    heappush(pq, [-(chance * nei_chance), nei])

        return ans
