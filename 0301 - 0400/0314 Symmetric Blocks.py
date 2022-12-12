class Solution:
    def solve(self, nums):
        if nums != sorted(nums, reverse=True): return False
        nums.append(0)

        last_height = 0
        cur_height = 0

        for i in range(len(nums)-1):
            num = nums[i]
            if i >= 1 and num != nums[i-1]:
                last_height = cur_height
            
            cur_height += 1
            if num-1 >= len(nums) or nums[num-1] < cur_height: return False
            if num >= len(nums) or nums[num] != last_height: return False

        return True
