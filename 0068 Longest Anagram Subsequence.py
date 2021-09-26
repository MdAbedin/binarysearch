class Solution:
    def solve(self, a, b):
        ca,cb = defaultdict(int,Counter(a)), defaultdict(int,Counter(b))
        return sum(min(ca[c], cb[c]) for c in ca)
