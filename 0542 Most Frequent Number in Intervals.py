class Solution:
    def solve(self, intervals):
        endpoints = sorted(list({x for interval in intervals for x in interval}))
        locs = {endpoints[i]:i for i in range(len(endpoints))}
        counts = [0]*(len(endpoints)+1)

        for l,r in intervals:
            counts[locs[l]] += 1
            counts[locs[r]+1] -= 1

        count = 0
        for i in range(len(counts)):
            count += counts[i]
            counts[i] = count

        return max(endpoints,key=lambda x: [counts[locs[x]],-x])
