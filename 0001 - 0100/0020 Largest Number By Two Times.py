class Solution:
    def solve(self, nums):
        nums.sort()
        
        biggest_number = nums[-1]
        second_biggest_number = nums[-2]

        return biggest_number > 2*second_biggest_number
