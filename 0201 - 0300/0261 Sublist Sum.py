class Solution:
    def solve(self, nums):
        total_sum = sum(nums)

        cur_sum = 0

        for num in nums:
            cur_sum = max(0, cur_sum + num)
            
            if cur_sum > total_sum:
                return True

        return False
