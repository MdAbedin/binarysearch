class Solution:
    def solve(self, n, enemies):
        g = defaultdict(list)

        for a,b in enemies:
            g[a].append(b)
            g[b].append(a)

        group1 = set()
        group2 = set()

        for i in range(n):
            if i in group1 or i in group2:
                continue

            cur_group = 1
            bfs = deque([i])
            group1.add(i)

            while bfs:
                for _ in range(len(bfs)):
                    cur = bfs.popleft()
                    
                    for nei in g[cur]:
                        if cur_group == 1:
                            if nei in group1:
                                return False

                            if nei not in group2:
                                group2.add(nei)
                                bfs.append(nei)
                        else:
                            if nei in group2:
                                return False

                            if nei not in group1:
                                group1.add(nei)
                                bfs.append(nei)

                cur_group = 2 if cur_group == 1 else 1

        return True
