class Solution:
    def solve(self, requests, k):
        starts = defaultdict(int)
        ends = defaultdict(int)

        for a,b in requests:
            starts[a] += 1
            ends[b] += 1

        starts = sorted(list(map(list,starts.items())))
        ends = sorted(list(map(list,ends.items())))

        for i in range(1,len(starts)):
            starts[i][1] += starts[i-1][1]
        
        for i in range(1,len(ends)):
            ends[i][1] += ends[i-1][1]

        ans = []

        for i in range(len(requests)):
            a,b = requests[i]

            earliest = ends[bisect_left(ends, [a,-1])-1][1] if bisect_left(ends, [a,-1])-1 >= 0 else 0
            latest = starts[bisect_right(starts, [b,inf])-1][1] - 1

            # print(i,a,b)
            # print(earliest, latest)

            if earliest <= k <= latest: ans.append(i)

        return ans
