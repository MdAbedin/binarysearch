class Solution:
    def solve(self, nums):
        locs = {0:-1}
        s=0
        ans=0
        for i in range(len(nums)):
          s+=nums[i]
          if s in locs:
            ans = max(ans,i-locs[s])
          else:
            locs[s]=i
        return ans
