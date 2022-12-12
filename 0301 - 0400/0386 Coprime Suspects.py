class Solution:
    def solve(self, a, b):
        if gcd(a,b) != 1: return 0
        if any(x != 1 for x in [gcd(a,b+1), gcd(a,b-1), gcd(a+1,b), gcd(a-1,b)]): return 1
        return 2
