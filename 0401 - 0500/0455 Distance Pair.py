class Solution:
    def solve(self, nums):
        if not nums:
            return 0

        pq = []

        for i in range(len(nums)):
            heappush(pq, [-(nums[i]-i), i])

        ans = -inf

        for i in range(len(nums)-1):
            while pq and pq[0][1] <= i:
                heappop(pq)

            ans = max(ans, nums[i]+i + -pq[0][0])

        return ans
