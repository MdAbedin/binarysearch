class Solution:
    def solve(self, fractions):
        counts = Counter((a//gcd(a,b), b//gcd(a,b)) for a,b in fractions)
        return sum(counts[(b-a,b)]*(counts[(a,b)] - (1 if b-a==a else 0)) for a,b in counts)//2
