class Solution:
    def solve(self, graph):
        s0, s1 = set(), set()

        for i in range(len(graph)):
            if i in s0 or i in s1: continue

            s0.add(i)
            bfs = deque([i])
            n = 0

            while bfs:
                for _ in range(len(bfs)):
                    cur = bfs.popleft()

                    for nei in graph[cur]:
                        if n == 1:
                            if nei in s1: return False
                            if nei not in s0:
                                s0.add(nei)
                                bfs.append(nei)
                        else:
                            if nei in s0: return False
                            if nei not in s1:
                                s1.add(nei)
                                bfs.append(nei)

                n = 1 - n
        
        return True
