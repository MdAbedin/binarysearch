class Solution:
    def solve(self, A, B, C):
        g = defaultdict(set)

        for a,b in C:
            g[a].add(b)
            g[b].add(a)

        seen = set()
        cycles = []

        def dfs(i, cycle):
            if i in seen: return

            seen.add(i)
            cycle.append(i)

            for nei in g[i]:
                dfs(nei,cycle)

        for i in range(len(A)):
            if i not in seen:
                cycle = []
                dfs(i,cycle)
                cycles.append(cycle)

        ans = 0

        for cycle in cycles:
            counts = Counter(A[i] for i in cycle)

            for i in cycle:
                if counts.get(B[i],0) > 0:
                    counts[B[i]] -= 1
                    ans += 1

        return ans
