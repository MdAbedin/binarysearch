class Solution:
    def solve(self, nums):
        is_strictly_increasing = True

        for i in range(len(nums)-1):
            if nums[i+1] <= nums[i]:
                is_strictly_increasing = False
                
        if is_strictly_increasing:
            return True

        is_strictly_decreasing = True

        # [5,4,6,2,1]
        for i in range(len(nums)-1):
            if nums[i+1] >= nums[i]:
                is_strictly_decreasing = False
                
        if is_strictly_decreasing:
            return True

        return False
