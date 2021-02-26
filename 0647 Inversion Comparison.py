class Solution:
    def helper(self, nums, l, r):
        if l == r: return 0
        ans = self.helper(nums, l, (l+r)//2) + self.helper(nums, (l+r)//2+1, r)
        j = (l+r)//2+1

        for i in range(l,(l+r)//2+1):
            while j <= r and nums[j] < nums[i]: j += 1
            ans += j - ((l+r)//2+1)

        nums[l:r+1] = sorted(nums[l:r+1])

        return ans

    def solve(self, nums):
        local_ans = sum(nums[i]>nums[i+1] for i in range(len(nums)-1))
        global_ans = self.helper(nums, 0, len(nums)-1)

        return local_ans == global_ans
