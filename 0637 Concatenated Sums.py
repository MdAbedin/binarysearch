class Solution:
    def solve(self, nums):
        ans = 0
        place_values = 0

        for num in nums:
            ans += num*len(nums)
            place_values += 10**len(str(num))

        ans += sum(nums)*place_values

        return ans
