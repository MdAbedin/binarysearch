class Solution:
    def solve(self, nums):
        if not nums:
            return 0
            
        hops = [inf]*len(nums)
        furthest = 0
        hops[0] = 0

        for i in range(len(nums)):
            for j in range(furthest+1,min(len(hops),i+nums[i]+1)):
                hops[j] = hops[i] + 1

            furthest = max(furthest, i+nums[i])

        return hops[-1]
