class Solution:
    def solve(self, intervals):
        endpoints = set()
        starts = defaultdict(int)
        ends = defaultdict(int)

        for l,r in intervals:
            endpoints.add(l)
            endpoints.add(r)
            starts[l] += 1
            ends[r] += 1

        concurrent = 0
        endpoints = sorted(list(endpoints))
        ans = 0

        for endpoint in endpoints:
            concurrent -= ends[endpoint]
            concurrent += starts[endpoint]
            ans = max(ans, concurrent)

        return ans
