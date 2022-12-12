class Solution:
    def solve(self, nums):
        min_pq = []
        max_pq = []

        for i,num in enumerate(nums):
            heappush(min_pq, [num, i])

        for i,num in enumerate(nums):
            heappush(max_pq, -num)

            while min_pq and min_pq[0][1] <= i:
                heappop(min_pq)

            if -max_pq[0] <= min_pq[0][0]:
                return i+1
