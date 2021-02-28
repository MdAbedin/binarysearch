class Solution:
    def solve(self, nums):
        if not nums: return 0
        
        dp = [inf]*len(nums)

        for i in range(len(nums)):
          num = nums[i]

          l,r = 0,len(dp)
          j = -1

          while l<=r:
            mid = (l+r)//2

            if num <= dp[mid]:
              j = mid
              r = mid-1
            else:
              l = mid+1

          dp[j] = num

        for i in range(len(dp)-1,-1,-1):
          if dp[i] != inf:
            return i+1
