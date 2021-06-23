class Solution:
    def solve(self, nums):
        ans = [-1]*len(nums)
        unmatched = []

        for i in range(len(nums)):
            while unmatched and unmatched[0][0] < nums[i]:
                ans[heappop(unmatched)[1]] = nums[i]

            heappush(unmatched, [nums[i], i])

        for i in range(len(nums)):
            while unmatched and unmatched[0][0] < nums[i]:
                ans[heappop(unmatched)[1]] = nums[i]

        return ans
