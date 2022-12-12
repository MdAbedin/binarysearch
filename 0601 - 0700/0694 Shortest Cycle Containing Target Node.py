class Solution:
    def solve(self, graph, target):
        seen = {target}
        bfs = deque([[target,0]])
        ans = inf

        while bfs:
            cur,i = bfs.popleft()

            for nei in graph[cur]:
                if nei == target: ans = min(ans, i+1)
                if nei in seen: continue
                bfs.append([nei,i+1])
                seen.add(nei)

        return -1 if ans == inf else ans
