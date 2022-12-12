class Solution:
    def solve(self, nums):
        if not nums: return 0
        if len(nums) == 1: return max(0,nums[0])

        dp = [0,0]

        for num in nums[:-1]:
            dp.append(max(dp[-1], dp[-2] + num))

        dp2 = [0,0]

        for num in nums[1:]:
            dp2.append(max(dp2[-1], dp2[-2] + num))

        return max(dp[-1], dp2[-1])
