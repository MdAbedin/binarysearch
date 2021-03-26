class Solution:
    def solve(self, nums):
        maxes = []
        mx = -inf

        for i in range(len(nums)-1,-1,-1):
            mx = max(mx, nums[i])
            maxes.append(mx)

        maxes.reverse()

        return sum(max(0,maxes[i]-nums[i]) for i in range(len(nums)))
