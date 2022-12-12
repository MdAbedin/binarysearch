class Solution:
    def solve(self, nums):
        if len(nums) < 2: return False

        lmax = nums[0]
        rmins = []
        rmin = nums[-1]
        for i in range(len(nums)-1,-1,-1):
            rmin = min(rmin, nums[i])
            rmins.append(rmin)
        rmins.reverse()

        for i in range(len(nums)-1):
            lmax = max(lmax, nums[i])
            if lmax < rmins[i+1]: return True
            
        return False
