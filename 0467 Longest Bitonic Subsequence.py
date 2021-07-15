class Solution:
    def solve(self, nums):
        l = [1]*len(nums)

        for i in range(len(nums)):
            l[i] = max((l[j] for j in range(i) if nums[j] < nums[i]),default=0)+1

        r = [1]*len(nums)

        for i in reversed(range(len(nums))):
            r[i] = max((r[j] for j in range(len(nums)-1,i,-1) if nums[j] < nums[i]),default=0)+1

        return max((l[i]+r[i]-1 for i in range(len(nums))),default=0)
