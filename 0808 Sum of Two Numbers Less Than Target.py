class Solution:
    def solve(self, nums, target):
        nums.sort()
        first,second = 0,len(nums)-1
        ans = -inf

        while first < second:
            while nums[first]+nums[second] >= target:
                second -= 1

            if second <= first: break

            ans = max(ans,nums[first]+nums[second])
            first += 1

        return ans
