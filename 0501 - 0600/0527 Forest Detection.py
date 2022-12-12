class Solution:
    def solve(self, edges):
        g = defaultdict(list)
        nodes = set()

        for a,b in edges:
            nodes.add(a)
            nodes.add(b)
            g[a].append(b)
            g[b].append(a)

        seen = set()

        for root in nodes:
            if root not in seen:
                seen.add(root)
                bfs = deque([[root,None]])

                while bfs:
                    cur,parent = bfs.popleft()

                    for nei in g[cur]:
                        if nei in seen:
                            if nei != parent: return False
                        else:
                            seen.add(nei)
                            bfs.append([nei,cur])

        return True
