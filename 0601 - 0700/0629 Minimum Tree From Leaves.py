class Solution:
    def solve(self, nums):
        @cache
        def helper(l,r):
            if l == r: return nums[l], nums[l]

            i = min(range(l,r), key = lambda i: helper(l,i)[0] + helper(i+1,r)[0])
            lsum,lmax = helper(l,i)
            rsum,rmax = helper(i+1,r)

            return lsum+rsum + lmax*rmax, max(lmax, rmax)

        return helper(0,len(nums)-1)[0]
