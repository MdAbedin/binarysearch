class Solution:
    def solve(self, s):
        counts = Counter(s)

        if sum(count%2 == 1 for count in counts.values()) > 1: return 0

        MOD = 10**9+7
        numerator = 1

        for i in range(len(s)//2):
            numerator *= (i+1)
            numerator %= MOD

        denominator = 1

        for count in counts.values():
            for i in range(count//2):
                denominator *= (i+1)
                denominator %= MOD

        return (numerator * pow(denominator, -1, MOD)) % MOD
