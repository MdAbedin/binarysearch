class Solution:
    def solve(self, nums, target):
        nums.sort()
        l,r = 0,len(nums)-1
        ans = inf

        while l < r:
            if nums[l]+nums[r] > target:
                ans = min(ans,nums[l]+nums[r])
                r -= 1
            else:
                l += 1
        
        return ans
