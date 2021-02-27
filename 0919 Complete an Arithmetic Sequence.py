class Solution:
    def solve(self, nums):
        if len(set(nums)) == 1: return nums[0]

        d = (nums[-1]-nums[0])//(len(nums))
        x = nums[0]+d
        nums = set(nums)

        while True:
          if x not in nums:
            return x
          x += d
