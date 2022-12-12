class Solution:
    def solve(self, nums):
        nums.sort()
        i = bisect_right(nums,0)
        expect = 1
        
        while i < len(nums):
            if nums[i] != expect: return expect
            expect += 1

            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1

            i += 1

        return expect
