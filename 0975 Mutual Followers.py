class Solution:
    def solve(self, relations):
        ans = set()
        g = defaultdict(set)

        for a,b in relations:
            g[a].add(b)

        for a,b in relations:
            if a in g[b]: ans.add(a)

        return sorted(list(ans))
