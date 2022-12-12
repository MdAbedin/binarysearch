class Solution:
    def solve(self, nums):
        if not nums: return 0

        nums2 = [[nums[i],i] for i in range(len(nums))]
        heapify(nums2)
        min_pq = nums2
        max_pq = []
        ans = 0

        for i in range(len(nums)):
            while min_pq and min_pq[0][1] <= i: heappop(min_pq)
            if (not max_pq or nums[i] > -max_pq[0]) and (not min_pq or nums[i] < min_pq[0][0]): ans += 1
            heappush(max_pq, -nums[i])

        return ans
