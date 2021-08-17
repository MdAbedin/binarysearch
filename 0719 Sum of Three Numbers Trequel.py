class Solution:
    def solve(self, nums):
        lefts = [-inf]*len(nums)
        nums_sorted = sorted([[nums[i],i] for i in range(len(nums))], reverse=True)
        unmatched = []

        for num,i in nums_sorted:
            while unmatched and i < -unmatched[0]:
                lefts[-heappop(unmatched)] = num

            heappush(unmatched, -i)

        rights = [-inf]*len(nums)
        mx = -inf

        for i in reversed(range(len(nums))):
            if mx >= nums[i]: rights[i] = mx
            mx = max(mx, nums[i])

        return max(lefts[i]+nums[i]+rights[i] for i in range(len(nums)))
