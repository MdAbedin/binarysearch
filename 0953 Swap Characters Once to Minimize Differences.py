class Solution:
    def solve(self, s, t):
        matches = sum(a==b for a,b in zip(s,t))
        mismatches = defaultdict(set)

        for a,b in zip(s,t):
            if a != b: mismatches[a].add(b)

        if any(b in mismatches and a in mismatches[b] for a in mismatches for b in mismatches[a]):
            return len(s) - (matches+2)

        if any(char in mismatches for a in mismatches for char in mismatches[a]):
            return len(s) - (matches+1)

        return len(s) - matches
