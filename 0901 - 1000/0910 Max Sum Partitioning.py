class Solution:
    def solve(self, nums, k):
        dp = [0]
        ans = 0
        
        for i in range(len(nums)):
          mx = nums[i]
          cur_ans = 0
          
          for j in range(i,max(-1,i-k),-1):
            mx = max(mx, nums[j])
            cur_ans = max(cur_ans, mx*(i-j+1) + dp[j])
            
          dp.append(cur_ans)
          ans = max(ans,cur_ans)
          
        return ans
