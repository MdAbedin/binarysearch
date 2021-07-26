class Solution:
    def solve(self, nums):
        uniques = set()
        j = 0
        ans = 0

        for i in range(len(nums)):
            while j < len(nums) and nums[j] not in uniques:
                uniques.add(nums[j])
                j += 1
                ans = max(ans, len(uniques))
            
            uniques.remove(nums[i])

        return ans
