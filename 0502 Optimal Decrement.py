class Solution:
    def solve(self, nums, k):
        pq = []

        for num in nums:
            heappush(pq,-num)

        for i in range(k):
            num = heappop(pq)
            heappush(pq,num+1)

        return -pq[0]
