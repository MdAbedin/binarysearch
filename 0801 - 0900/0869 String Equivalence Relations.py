class Solution:
    def solve(self, e, f, target):
        g = defaultdict(set)
        for a,b in zip(e,f):
            g[a].add(b)
            g[b].add(a)
        
        seen = set()
        classes = defaultdict(set)
        leaders = dict()

        for c in f:
            if c in seen: continue
            seen.add(c)
            dfs = [c]

            while dfs:
                cur = dfs.pop()
                classes[c].add(cur)
                leaders[cur] = c

                for nei in g[cur]:
                    if nei not in seen:
                        seen.add(nei)
                        dfs.append(nei)

        mins = {key:min(classes[key]) for key in classes}
        return "".join(mins[leaders[c]] if c in leaders else c for c in target)
