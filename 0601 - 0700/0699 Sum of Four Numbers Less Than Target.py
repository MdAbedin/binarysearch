class Solution:
    def solve(self,a,b,c,d,target):
        counts_ab, counts_cd = defaultdict(int), defaultdict(int)

        for i in range(len(a)):
            for j in range(len(b)):
                counts_ab[a[i] + b[j]] += 1

        for i in range(len(c)):
            for j in range(len(d)):
                counts_cd[c[i] + d[j]] += 1

        counts_ab = sorted(list(item) for item in counts_ab.items())
        counts_cd = sorted(list(item) for item in counts_cd.items())
        j = len(counts_cd)-1
        ans = 0

        for i in range(1,len(counts_cd)):
            counts_cd[i][1] += counts_cd[i-1][1]

        for pair_sum, count in counts_ab:
            while j >= 0 and pair_sum + counts_cd[j][0] > target: j -= 1
            if j < 0: break
            ans += count * counts_cd[j][1]

        return ans
