class Solution:
    def solve(self, nums):
        l,r = 0,len(nums)-1
        ans = inf

        while l <= r:
            mid = (l+r)//2

            if mid == nums[mid]:
                ans = min(ans, mid)
                r = mid-1
            if mid < nums[mid]:
                r = mid-1
            if mid > nums[mid]:
                l = mid+1

        return -1 if ans == inf else ans
