class Solution:
    def solve(self, nums, queries):
      
      ans = [[1,float("inf")]]
      
      for i in range(1,len(nums)):
        if nums[i]-nums[i-1] == ans[-1][1]:
          ans.append([ans[-1][0]+1,ans[-1][1]])
        else:
          ans.append([2,nums[i]-nums[i-1]])
          
      print(ans)
      return sum(ans[r][0] >= r-l+1 for l,r in queries)
