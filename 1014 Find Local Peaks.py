class Solution:
    def solve(self, nums):
        if len(nums) == 1: return []
        return list(filter(lambda i:(nums[i] > nums[i-1] if i > 0 else True) and (nums[i] > nums[i+1] if i < len(nums)-1 else True), range(len(nums))))
