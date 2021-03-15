class Solution:
    def solve(self, nums):
        nums_sorted = sorted(nums.copy())

        for i in range(len(nums)):
            if nums[i] != nums_sorted[i]:
                for j in range(len(nums)-1,-1,-1):
                    if nums[j] != nums_sorted[j]:
                        return j-i+1

        return 0
