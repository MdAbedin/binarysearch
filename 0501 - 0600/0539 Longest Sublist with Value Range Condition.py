class Solution:
    def solve(self, nums):
        if not nums:
            return 0

        min_pq = []
        max_pq = []
        j = -1

        if set(nums) == {0}:
            return 0

        ans = 1

        for i in range(len(nums)):
            while min_pq and min_pq[0][1] < i:
                heappop(min_pq)

            while max_pq and max_pq[0][1] < i:
                heappop(max_pq)

            if j < i:
                j = i
                heappush(min_pq, [nums[i], i])
                heappush(max_pq, [-nums[i], i])

            while j+1 < len(nums) and 2*min(min_pq[0][0],nums[j+1]) > max(-max_pq[0][0], nums[j+1]):
                heappush(min_pq, [nums[j+1], j+1])
                heappush(max_pq, [-nums[j+1], j+1])
                ans = max(ans, j+1-i+1)
                j += 1

        return ans
