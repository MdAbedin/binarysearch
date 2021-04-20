class Solution:
    def solve(self, heights, k):
        pq = []
        ans = []

        for i in range(len(heights)-1,-1,-1):
            while pq and pq[0][1] > i+k: heappop(pq)
            if not pq or heights[i] > -pq[0][0]: ans.append(i)
            heappush(pq, [-heights[i],i])

        return sorted(ans)
