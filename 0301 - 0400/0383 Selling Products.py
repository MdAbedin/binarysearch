class Solution:
    def solve(self, items, n):
        counts = Counter(items).most_common()[::-1]
        # print(counts)

        for i in range(len(counts)):
            if n-counts[i][1] < 0: return len(counts)-i
            n -= counts[i][1]

        return 0
