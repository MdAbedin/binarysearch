class Solution:
    def solve(self, nums):
        boundary = -1
        skips = 0

        for i in range(len(nums)):
            if boundary >= 1 and nums[boundary-1] == nums[boundary] == nums[i]:
                skips += 1
            else:
                boundary += 1
                nums[boundary], nums[i] = nums[i], nums[boundary]

        for _ in range(skips): nums.pop()

        return nums
