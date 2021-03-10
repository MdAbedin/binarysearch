class Solution:
    def solve(self, nums):
        mn = nums[0]

        for i in range(len(nums)):
            old = nums[i]
            nums[i] = mn
            mn = min(mn, old)

        nums[0]=0

        return nums
