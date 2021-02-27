class Solution:
    def solve(self, nums):
        left_sum = 0
        right_sum = sum(nums[1:])

        for i in range(len(nums)):
            if left_sum == right_sum:
                return i

            if i == len(nums)-1:
                break
                
            left_sum += nums[i]
            right_sum -= nums[i+1]

        return -1
