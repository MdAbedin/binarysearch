class Solution:
    def solve(self, nums, k):
        mods = [0]*k
        ans = 0
        
        for n in nums:
          ans += mods[(k-n)%k]
          mods[n%k]+=1
          
        return ans
