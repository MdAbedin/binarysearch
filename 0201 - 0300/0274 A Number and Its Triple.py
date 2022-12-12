class Solution:
    def solve(self, nums):
        counts = Counter(nums)
        
        for num in counts:
            if num == 0:
                if counts[0] > 1: return True
            elif num*3 in nums: return True

        return False
