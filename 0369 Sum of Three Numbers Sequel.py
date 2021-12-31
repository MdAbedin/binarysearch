class Solution:
    def solve(self, nums, k):
        nums.sort()
        rights = copy.copy(nums)
        ans = inf

        for i in range(len(nums)):
            rights.pop(0)

            for j in range(i):
                idx = bisect_left(rights, k - nums[i] - nums[j])
                
                if idx in range(len(rights)):
                    ans = min(ans, abs(nums[i] + nums[j] + rights[idx] - k))

                if idx-1 in range(len(rights)):
                    ans = min(ans, abs(nums[i] + nums[j] + rights[idx-1] - k))

        return ans
