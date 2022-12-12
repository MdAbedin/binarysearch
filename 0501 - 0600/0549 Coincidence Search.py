class Solution:
    def solve(self, nums):
        ans = 0

        for num in nums:
            lo = 0
            hi = len(nums) - 1

            while lo <= hi:
                mid = floor((lo + hi) / 2)
                if nums[mid] == num:
                    ans += 1
                    break
                elif nums[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return ans
