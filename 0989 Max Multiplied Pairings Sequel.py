class Solution:
    def solve(self, nums, multipliers):
        @cache
        def helper(l,r):
            i = l + (len(nums)-1-r)
            if i == len(multipliers)-1: return max(multipliers[i] * nums[l], multipliers[i] * nums[r])
            return max(multipliers[i] * nums[l] + helper(l+1,r), multipliers[i] * nums[r] + helper(l,r-1))

        return helper(0,len(nums)-1)
