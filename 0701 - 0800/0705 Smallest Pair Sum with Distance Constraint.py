class Solution:
    def solve(self, nums):
        mins = []
        mn = inf

        for i in range(len(nums)-1,-1,-1):
            mn = min(mn, nums[i])
            mins.append(mn)

        mins.reverse()

        return min(nums[i] + mins[i+2] for i in range(len(nums)-2))
