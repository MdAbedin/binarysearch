class Solution:
    def solve(self, nums):
        if all(nums[i]>=nums[i-1] for i in range(1,len(nums))): return 0
        
        ls = [0]*len(nums)
        ls[0]=1
        for i in range(1,len(nums)):
          if nums[i] >= nums[i-1]:
            ls[i] = 1
          else:
            break
          
        rs = [0]*len(nums)
        rs[-1]=1
        for i in range(len(nums)-2,-1,-1):
          if nums[i] <= nums[i+1]:
            rs[i] = 1
          else:
            break
          
        print(ls)
        print(rs)
        def works(x):
          return (x < len(nums) and (rs[x]==1 or ls[len(nums)-x-1]==1)) or any(ls[i-1]==1 and rs[i+x]==1 and nums[i-1]<=nums[i+x] for i in range(1,len(nums)-x))
        
        l,r = 1,len(nums)
        ans = -1
        
        while l <= r:
          mid = (l+r)//2
          
          if works(mid):
            ans = mid
            r = mid - 1
          else:
            l = mid+1
            
        return ans
