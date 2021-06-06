class Solution:
    def solve(self, stairs, k):
        if len(stairs) == 1:
            return stairs[0]
            
        pq = [[stairs[0], 0]]

        for i in range(1,len(stairs)):
            while pq[0][1] < i-k:
                heappop(pq)

            if i == len(stairs)-1:
                return pq[0][0]+stairs[-1]

            heappush(pq, [pq[0][0]+stairs[i], i])
