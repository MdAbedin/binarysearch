class Solution:
    def solve(self, k, nums):
      if not k: return 0
      counts = defaultdict(int)
      distincts = 0
      r = 0

      while r < len(nums) and not(distincts == k and not counts[nums[r]]):
        if not counts[nums[r]]: distincts += 1
        counts[nums[r]] += 1
        r += 1

      ans = r

      for l in range(1,len(nums)):
        counts[nums[l-1]] -= 1
        if not counts[nums[l-1]]: distincts -= 1
        
        while r < len(nums) and not(distincts == k and not counts[nums[r]]):
          if not counts[nums[r]]: distincts += 1
          counts[nums[r]] += 1
          r += 1

        ans = max(ans, r-l)

      return ans
