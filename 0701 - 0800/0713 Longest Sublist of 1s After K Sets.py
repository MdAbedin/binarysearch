class Solution:
    def solve(self, nums, k):
        if not nums: return 0
        if nums.count(0) <= k: return len(nums)

        locs = [-1]+[i for i in range(len(nums)) if nums[i] == 0]+[len(nums)]
        ans = -1

        for i in range(k,len(locs)-1):
            ans = max(ans, locs[i+1]-locs[i-k]-1)

        return ans
