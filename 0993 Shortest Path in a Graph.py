class Solution:
    def solve(self, edges, start, end):
        g = defaultdict(list)

        for u,v,w in edges:
            g[u].append([v,w])

        pq = [[0,start]]
        bests = defaultdict(lambda: inf)

        while pq:
            cost,cur = heappop(pq)

            if cost > bests[cur]:
                continue

            if cur == end:
                return cost

            for nei,w in g[cur]:
                if cost + w < bests[nei]:
                    bests[nei] = cost + w
                    heappush(pq, [cost+w, nei])

        return -1
