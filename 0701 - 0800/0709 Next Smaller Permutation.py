class Solution:
    def solve(self, nums):
        min_num = inf

        for i in reversed(range(len(nums))):
            if nums[i] > min_num:
                swap_i = max((j for j in range(i+1,len(nums)) if nums[j] < nums[i]), key = lambda j: nums[j])
                nums[i], nums[swap_i] = nums[swap_i], nums[i]
                break
            else:
                min_num = nums[i]
                min_num_i = i

        return nums
