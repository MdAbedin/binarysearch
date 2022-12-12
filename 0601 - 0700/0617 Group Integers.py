class Solution:
    def solve(self, nums):
        nums.sort()

        for i in range(2,len(nums)+1):
            if len(nums)%i == 0 and all(all(nums[j+k] == nums[j] for k in range(i)) for j in range(0,len(nums),i)): return True

        return False
