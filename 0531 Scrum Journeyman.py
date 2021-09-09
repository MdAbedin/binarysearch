class Solution:
    def solve(self, intervals, types):
        sorted_endpoints = sorted(list({end for interval in intervals for end in interval}))
        counts = defaultdict(int)

        for start, end in intervals:
            counts[start] += 1
            counts[end] -= 1

        counts = dict(zip(sorted_endpoints, accumulate(x[1] for x in sorted(counts.items()))))
        ans = []
        cur_count = 0

        for end in sorted_endpoints:
            if cur_count != 0: ans[-1][1] = end
            cur_count = counts[end]
            if cur_count != 0: ans.append([end, None, cur_count])

        return ans
