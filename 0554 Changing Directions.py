class Solution:
    def solve(self, nums):
        if not nums: return 0
        nums = [nums[0]] + nums + [nums[-1]]
        return sum((nums[i]-nums[i-1]) * (nums[i+1]-nums[i]) < 0 for i in range(1,len(nums)-1))
