class Solution:
    def solve(self, nums, k):
        nums.sort()
        if k == 0: return nums[-1]-nums[0]

        return min(nums[i+len(nums)-k-1]-nums[i] for i in range(k+1))
