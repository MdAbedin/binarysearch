class Solution:
    def solve(self, source, target, sources, targets, rates):
        g = defaultdict(list)
        for s,t,r in zip(sources,targets,rates):
            g[s].append([t,r])

        dfs = [[source,1]]
        maxes = defaultdict(lambda: -inf)
        maxes[source] = 1
        seen = set()
        ans = -inf

        while dfs:
            cur,val = dfs[-1]

            if cur in seen:
                if cur == target: ans = max(ans, val)
                seen.remove(cur)
                maxes[cur] = -inf
                dfs.pop()
            else:
                seen.add(cur)
                maxes[cur] = val
                for t,r in g[cur]:
                    if val*r > maxes[t]:
                        if t in seen: return -1
                        dfs.append([t,val*r])
                        maxes[t] = val*r

        return max(0,ans)
