class Solution:
    def solve(self, nums, target):
        if not target: return 0
        MOD = int(1e9+7)
        counts = defaultdict(int)
        count = 0
        target = set(target)
        ans = 0
        j = 0
        
        for i in range(len(nums)):
          j = max(i,j)
          while j < len(nums) and not (count == len(target) or (count == len(target)-1 and nums[j] in target and counts[nums[j]] == 0)):
            if nums[j] in target:
              if counts[nums[j]] == 0: count += 1
              counts[nums[j]] += 1
            j += 1
          
          ans += (j-i)%MOD
          ans = ans%MOD
          #ans = (ans-1)%MOD
          
          if nums[i] in target and counts[nums[i]]!=0:
            counts[nums[i]] -= 1
            if counts[nums[i]] == 0:
              count -= 1
              
        return ans
