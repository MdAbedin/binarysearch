class Solution:
    def solve(self, s, t):
        counts_s,counts_t = defaultdict(int,Counter(s)),defaultdict(int,Counter(t))

        return len(s)-sum(min(counts_t[char],counts_s[char]) for char in counts_t)
