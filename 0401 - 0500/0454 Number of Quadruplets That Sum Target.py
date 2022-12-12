class Solution:
    def solve(self, a, b, c, d, target):
        counts_ab, counts_cd = defaultdict(int), defaultdict(int)

        for i in range(len(a)):
            for j in range(len(b)):
                counts_ab[a[i] + b[j]] += 1

        for i in range(len(c)):
            for j in range(len(d)):
                counts_cd[c[i] + d[j]] += 1

        ans = 0

        for pair_sum, count in counts_ab.items():
            ans += count * counts_cd[target - pair_sum]

        return ans
