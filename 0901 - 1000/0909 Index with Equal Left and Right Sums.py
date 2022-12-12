class Solution:
    def solve(self, nums):
        total_sum = sum(nums)
        lsum = 0

        for i in range(len(nums)):
          if lsum == total_sum - lsum - nums[i]: return i
          lsum += nums[i]

        return -1
