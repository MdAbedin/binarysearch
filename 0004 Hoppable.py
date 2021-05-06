class Solution:
    def solve(self, nums):
        furthest = 0

        for i in range(len(nums)):
            if i > furthest:
                return False

            if i == len(nums)-1:
                return True

            furthest = max(furthest, i+nums[i])
