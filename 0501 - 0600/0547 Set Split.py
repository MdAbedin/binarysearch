class Solution:
    def solve(self, nums):
        nums.sort()
        psums = nums[:]
        for i in range(1,len(nums)):
            psums[i] += psums[i-1]
        return any(psums[i] == psums[-1]-psums[i] and nums[i]!=nums[i+1] for i in range(len(nums)-1))
