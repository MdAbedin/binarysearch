class Solution:
    def solve(self, nums, k):
        nums.sort()
        return min(nums[i]-nums[i-k+1] for i in range(k-1,len(nums)))
