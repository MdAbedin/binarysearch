class Solution:
    def solve(self, nums):
        uniques = set()
        j = -1
        ans = 0
        cur_sum = 0

        for i in range(len(nums)):
            while j+1 < len(nums) and nums[j+1] not in uniques:
                uniques.add(nums[j+1])
                cur_sum += nums[j+1]
                ans = max(ans, cur_sum)
                j += 1

            uniques.remove(nums[i])
            cur_sum -= nums[i]

        return ans
